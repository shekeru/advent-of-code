module Main where

import Control.Monad
import Data.Function
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
      print $ map _units [fst x, snd x]

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
  ideal = minimumBy (targOrder actor) rxs in Offense
    ((actor, ideal) : bxs) (delete ideal rxs)

targOrder :: Group -> Group -> Group -> Ordering
targOrder atk = on (flip compare) calc where
  calc x = _initiative x + 40 * trueDmg atk x

trueDmg :: Group -> Group -> Int
trueDmg atk def
  | _attackType atk `elem` _immunities def = 0
  | _attackType atk `elem` _weaknesses def = 2 * dmg
  | otherwise = dmg where dmg = _attackDamage atk * _units atk

atkOrder :: Group -> Group -> Ordering
atkOrder = on (flip compare) _initiative

-- selOrder :: Group -> Group -> Ordering
-- selOrder = on (flip compare) calc where
--   calc x = _initiative x + 40 *
--     (_units x * _attackDamage x)
