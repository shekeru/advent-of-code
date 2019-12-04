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
      sorted = sortBy (on orderAtk fst)

main :: IO()
main = do
    groups <- Input.getFile
    printf "Silver: %d\n"
      (solve battle groups)
    -- forM_ (take 20 $ iterate (conduct.matched) groups) $ \ys -> do
    --   print $ sort $ map _units ys
    printf "Gold: %d\n"
      (solve survive groups)
    where solve fn xs = sum $ map _units (fn xs)

    -- forM_ (_battles $ matched groups ) $ \x ->
    --   print (_units $ fst x, _units $ snd x)
    -- forM_ (take 60 $ iterate (conduct.matched) $ bxs !! 1570) $ \ys -> do
    --   print $ map _units ys
    -- printf "Gold: %d\n"
    -- forM_ ys print
    -- forM_ (_battles (matched $ bxs !! 1570)) $ \x ->
    --   print (_units $ fst x, _units $ snd x)
    -- forM_ (conduct $ matched ys) print

survive :: [Group] -> [Group]
survive = head.dropWhile fn.map battle.iterate
  (map boost) where fn = ("Infection" ==)._system.head

boost :: Group -> Group
boost x = if "Infection" /= _system x then
  x{_attackDamage = _attackDamage x + 1} else x

battle :: [Group] -> [Group]
battle = head.dropWhile fn.iterate (conduct.matched)
  where fn = (>1).length.nub.map _system

conduct :: Offense -> [Group]
conduct (Offense bxs rxs) = prepare $ foldl execute rxs bxs where
  execute rxs' (atk, def) = (if _units atk' <= 0 then def else def{_units
      = _units def - div (trueDmg atk' def) (_hitPoints def)}) : rxs'
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
  (Offense [] def) (sortBy orderEff atk)

selection :: Offense -> Group -> Offense
selection rets@(Offense bxs []) _ = rets
selection rets@(Offense bxs rxs) actor
  | trueDmg actor ideal == 0 = rets
  | otherwise = Offense ((actor, ideal) : bxs) (delete ideal rxs)
    where ideal = minimumBy (oTarget actor) rxs

trueDmg :: Group -> Group -> Int
trueDmg atk def
  | _attackType atk `elem` _immunities def = 0
  | _attackType atk `elem` _weaknesses def = 2 * effdmg atk
  | otherwise = effdmg atk

effdmg :: Group -> Int
effdmg x = _attackDamage x * _units x

oTarget :: Group -> Group -> Group -> Ordering
oTarget atk = on (flip compare)
  (trueDmg atk) <> orderEff

orderEff :: Group -> Group -> Ordering
orderEff =  on (flip compare) effdmg <> orderAtk

orderAtk :: Group -> Group -> Ordering
orderAtk = on (flip compare) _initiative
