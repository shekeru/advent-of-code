{-# LANGUAGE PartialTypeSignatures, TemplateHaskell #-}
module Main where

import Data.List
import Data.Function
--import qualified Data.Map.Strict as SM
import qualified Data.Map.Strict as LM
import Control.Monad
import Control.Lens
import Data.Maybe

import Debug.Trace
import Text.Printf

data Faction = Goblin | Elves deriving (Show, Eq)
type Overlay = LM.Map Coords [Coords]
type Units = LM.Map Coords Mob
type Coords = (Int, Int)
type Space = [[Bool]]
data Mob = Unit {
  _side :: Faction, _hp :: Int, _dmg :: Int
} deriving (Show, Eq)
makeLenses ''Mob

main = do
  silver <- system <$> input
  printf "Silver: %d\n" silver

input :: IO (Space, Units)
input = do
  xss <- lines <$> readFile "input.txt"
  let parse (y,_,v) = mapAccumL addTile (y+1, 0, v)
  let ((_,_, carts), tracks) = mapAccumL parse (-1, 0, LM.empty) xss
  return (tracks, carts)

addTile :: (Int, Int, Units) -> Char -> ((Int, Int, Units), Bool)
addTile acc 'G' = (extract acc (Unit Goblin 200 3), True)
addTile acc 'E' = (extract acc (Unit Elves 200 3), True)
addTile (y,x,tiles) c = ((y, x+1, tiles), c == '.')

extract :: (Int, Int, Units) -> Mob -> (Int, Int, Units)
extract (y, x, units) mob = (y, x+1, LM.insert (y, x) mob units)

adj :: Space -> Units -> Coords -> [Coords]
adj space units (y,x) = [crds | crds <- [
  (y-1, x), (y, x-1), (y, x+1), (y+1, x)], (null space
    || check crds space) && LM.notMember crds units]

check :: Coords -> Space -> Bool
check (y,x) vs = (y >= 0) && (x >= 0) && (y < length vs)
  && (x < length (vs !! y)) && ((vs !! y) !! x)

team vs f y = LM.filter (on f _side y) vs

select :: Units -> Coords -> Maybe Coords
select units mob = listToMaybe $ sortOn metric $
  filter (`LM.member` units) $ adj [] LM.empty mob
    where metric key = _hp (units LM.! key)

slots :: Space -> Units -> Mob -> [Coords]
slots space units mob = concatMap (adj space units)
  (LM.keys $ team units (/=) mob)

moves :: Space -> Units -> [Coords] -> Overlay -> Coords -> Overlay
moves space units valid sys crds = LM.unionsWith (\a b -> if length a <=
  length b then a else b) $ sys : [bfs next | next <- adj space units crds,
    next `LM.notMember` sys, all (`notElem` valid) $ LM.keys sys] where
  sys' key = LM.insert key (key : (LM.findWithDefault [] crds sys)) sys
  bfs next = moves space units valid (sys' next) next

damage :: Mob -> Maybe Mob -> Maybe Mob
damage agg (Just def) = if _hp def' > 0 then Just def'
  else Nothing where def' = def & hp -~ (agg ^. dmg)

silver :: Space -> (Bool, Units) -> Coords -> Mob -> (Bool, Units)
silver space (True, units) key mob = (not (LM.null $ team units (/=) mob),
   turn space units key)
silver space (False, units) key mob = (False, units)

turn :: Space -> Units -> Coords -> Units
turn space units key = if (traceShowId key) `LM.member` units then do
  let (mob, units') = traceShowId $ (units LM.! key, LM.delete key units)
  case select (team units (/=) mob) key of
    Just attack -> LM.alter (damage mob) attack units
    Nothing -> do
    let (valid, start) = traceShowId $ (slots space units' mob, LM.fromList [(key, [])])
    let opts = if key `elem` valid then start else
          moves space units' valid start key
    let targets = valid `intersect` LM.keys opts
    let move = case listToMaybe $ sortOn (length.(opts LM.!)) targets of
          Just path -> last $ key : opts LM.! path; Nothing -> key
    let forwards = LM.insert move mob units'
    case select (team forwards (/=) mob) move of
      Just attack -> LM.alter (damage mob) attack forwards
      Nothing -> forwards
  else units

system :: (Space, Units) -> _
system (space, units) = solve.head.dropWhile (snd.fst) $ iterate partial ((0, True), units) where
  partial ((int, bool), xs) = ((if bool' then int + 1 else int, bool'), ys) where
    (bool', ys) = LM.foldlWithKey (silver space) (bool, xs) xs
  solve ((int, bool), xs) = int * LM.foldr (\a b -> _hp a + b) 0 xs

-- test = do
--   (space, units) <- input
--   let key = (2, 1)
--   pure $ moves space units (LM.singleton key []) key
