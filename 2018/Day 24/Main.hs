module Main where

import Text.Printf
import Control.Monad
import Data.Function
import Data.Ord
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
      sorted = sortBy (on (flip orderAtk) fst)

main :: IO()
main = do
    groups <- Input.getFile
    printf "Silver: %d\n"
      (sum $ map _units $ battle groups)
    let bxs = iterate (map boost) groups
    forM_ (take 60 $ iterate (conduct.matched) $ bxs !! 1570) $ \ys -> do
      print $ map _units ys
    -- printf "Gold: %d\n"
    -- forM_ ys print
    -- forM_ (_battles (matched $ bxs !! 1570)) $ \x ->
    --   print (_units $ fst x, _units $ snd x)
    -- forM_ (conduct $ matched ys) print

-- nigs = map battle.
--   where fn = ("Infection" ==)._system.head

boost :: Group -> Group
boost x = if "Infection" /= _system x then
  x{_attackDamage = _attackDamage x + 1} else x

battle :: [Group] -> [Group]
battle = head.dropWhile fn.iterate (conduct.matched)
  where fn = (>1).length.nub.map _system

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
assign atk def = foldl selection (Offense [] def)
  (sortBy (flip orderEff) atk)

selection :: Offense -> Group -> Offense
selection rets@(Offense bxs []) _ = rets
selection (Offense bxs rxs) actor = let
  ideal = maximumBy (oTarget actor) rxs in Offense
    ((actor, ideal) : bxs) (delete ideal rxs)

trueDmg :: Group -> Group -> Int
trueDmg atk def
  | _attackType atk `elem` _immunities def = 0
  | _attackType atk `elem` _weaknesses def = 2 * dmg atk
  | otherwise = dmg atk

oTarget :: Group -> Group -> Group -> Ordering
oTarget atk = comparing (trueDmg atk) <> orderEff

dmg :: Group -> Int
dmg x = _attackDamage x * _units x

orderEff :: Group -> Group -> Ordering
orderEff = comparing dmg <> orderAtk

orderAtk :: Group -> Group -> Ordering
orderAtk = comparing _initiative
