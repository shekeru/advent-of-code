module Main where

import Text.Printf
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
    printf "Silver: %d\n"
      (part1 groups)
    -- forM_ ys print
    -- forM_ (_battles $ matched ys) $ \x ->
    --   print (_units $ fst x, _units $ snd x)
    -- forM_ (conduct $ matched ys) print

part1 :: [Group] -> Int
part1 = sum.map _units.head.battle where
  battle = dropWhile fn.iterate (conduct.matched)
  fn = (>1).length.nub.map _system

conduct :: Offense -> [Group]
conduct (Offense bxs rxs) = prepare $ foldl execute rxs bxs where
  execute rxs' (atk, def) = def {_units = _units def
    - div (trueDmg atk' def) (_hitPoints def)} : rxs'
    where atk' = fromMaybe atk (find (atk ==) rxs')
  prepare = filter (\y -> _units y > 0)

matched :: [Group] -> Offense
matched groups = do
    let immune = filter cmp groups
    let hostile = filter (not.cmp) groups
    assign immune hostile <> assign hostile immune
      where cmp x = "Infection" /= _system x

assign :: [Group] -> [Group] -> Offense
assign atk def = foldl selection
  (Offense [] def) (sortBy selOrder atk)

selection :: Offense -> Group -> Offense
selection rets@(Offense bxs []) _ = rets
selection (Offense bxs rxs) actor = let
  ideal = maximumBy (targOrder actor) rxs in Offense
    ((actor, ideal) : bxs) (delete ideal rxs)

targOrder :: Group -> Group -> Group -> Ordering
targOrder atk = on compare calc where
  calc x = _initiative x + 21 *
    dmg x + 2100 * trueDmg atk x

trueDmg :: Group -> Group -> Int
trueDmg atk def
  | _attackType atk `elem` _immunities def = 0
  | _attackType atk `elem` _weaknesses def = 2 * dmg atk
  | otherwise = dmg atk

dmg :: Group -> Int
dmg x = _attackDamage x * _units x

atkOrder :: Group -> Group -> Ordering
atkOrder = on (flip compare) _initiative

selOrder :: Group -> Group -> Ordering
selOrder = on (flip compare) calc where
  calc x = _initiative x + 21 * dmg x
