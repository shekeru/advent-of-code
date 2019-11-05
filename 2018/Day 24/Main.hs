module Main where

import Debug.Trace

import Control.Monad
import Data.Function
import Data.Maybe
import Data.List
import Input

data Offense = Offense {
  _battles :: [(Group, Group)],
  _remaining :: [Group]
} deriving (Show)

instance Semigroup Offense where
  xs <> ys = Offense
    (sorted $ on (++) _battles xs ys)
    (on (++) _remaining xs ys) where
      sorted = sortBy (on atkOrder fst)

main :: IO()
main = do
    groups <- sortBy atkOrder
      <$> Input.getFile
    forM_ (_battles $ matched groups) $ \x ->
      print (_units $ fst x, _units $ snd x)

conduct :: Offense -> [Group]
conduct (Offense bxs rxs) = reverse $ foldl execute rxs bxs where
  execute rxs' (atk, def) = def {_units = _units def
    - div (trueDmg atk' def) (_hitPoints def)} : rxs'
    where atk' = fromMaybe atk (find (atk ==) rxs')

matched :: [Group] -> Offense
matched groups = do
    let immune = filter cmp groups
    let hostile = filter (not.cmp) groups
    assign immune hostile <> assign hostile immune
      where cmp x = "Infection" /= _system x

assign :: [Group] -> [Group] -> Offense
assign atk def = foldl selection
  (Offense [] def) (sortBy atkOrder atk)

selection :: Offense -> Group -> Offense
selection rets@(Offense bxs []) _ = rets
selection (Offense bxs rxs) actor = let
  ideal = maximumBy (targOrder actor) rxs in Offense
    ((actor, ideal) : bxs) (delete ideal rxs)

targOrder :: Group -> Group -> Group -> Ordering
targOrder atk = on compare calc where
  calc x = _initiative x + 40 * trueDmg atk x

trueDmg :: Group -> Group -> Int
trueDmg atk def
  | _attackType atk `elem` _immunities def = 0
  | _attackType atk `elem` _weaknesses def = 2 * dmg
  | otherwise = dmg where
    dmg = traceShow (_units atk, _units def, _attackDamage atk * _units atk) _attackDamage atk * _units atk

atkOrder :: Group -> Group -> Ordering
atkOrder = on (flip compare) _initiative
