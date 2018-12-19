{-# LANGUAGE PartialTypeSignatures, TemplateHaskell #-}
module Main where

import Data.List
import Data.Function
import qualified Data.Map.Strict as SM
import Control.Monad
import Control.Lens
import Data.Maybe

import Debug.Trace

data Faction = Goblin | Elf deriving (Show, Eq)
type Overlay = SM.Map Coords [Coords]
type Units = SM.Map Coords Mob
type Coords = (Int, Int)
type Space = [[Bool]]
data Mob = Unit {
  _side :: Faction, _hp :: Int, _dmg :: Int
} deriving (Show, Eq)
makeLenses ''Mob

main = print ""

input :: IO (Space, Units)
input = do
  xss <- lines <$> readFile "test0.txt"
  let parse (y,_,v) = mapAccumL addTile (y+1, 0, v)
  let ((_,_, carts), tracks) = mapAccumL parse (-1, 0, SM.empty) xss
  return (tracks, carts)

addTile :: (Int, Int, Units) -> Char -> ((Int, Int, Units), Bool)
addTile acc 'G' = (extract acc (Unit Goblin 200 3), True)
addTile acc 'E' = (extract acc (Unit Elf 200 3), True)
addTile (y,x,tiles) c = ((y, x+1, tiles), c == '.')

extract :: (Int, Int, Units) -> Mob -> (Int, Int, Units)
extract (y, x, units) mob = (y, x+1, SM.insert (y, x) mob units)

adj :: Space -> Units -> Coords -> [Coords]
adj space units (y,x) = [crds | crds <- [
    (y-1, x), (y, x-1), (y, x+1), (y+1, x)
  ], check crds space && SM.notMember crds units]

check :: Coords -> Space -> Bool
check (y,x) vs = (y >= 0) && (x >= 0) && (y < length vs)
  && (x < length (vs !! y)) && ((vs !! y) !! x)

enemy :: Units -> Mob -> Units
enemy vs unit = SM.filter opposing vs where
  opposing x = _side unit /= _side x

select :: Units -> Coords -> Maybe Coords
select units (y, x) = listToMaybe $ sortOn f [crds |
  crds <- [(y-1, x), (y, x-1), (y, x+1), (y+1, x)],
  SM.member crds units] where f k = _hp (units SM.! k)

slots :: Space -> Units -> Mob -> [Coords]
slots space units mob = concatMap (adj space units) (SM.keys $ enemy units mob)

moves :: Space -> Units -> [Coords] -> Overlay -> Coords -> Overlay
moves space units xs sys crds = foldl (moves space units $ crds:xs) sys' next' where
   next' = adj space units crds \\ SM.keys sys; sys' = SM.insert crds xs sys

build :: Space -> Units -> Overlay -> Coords -> Overlay
build space units sys crds = case prev of
  Just prev -> SM.insert crds (crds:prev) sys
  Nothing -> sys; where
    eval next = (build space units sys next) SM.!
      next
    prev = listToMaybe $ [eval next | next
      <- (reverse $ adj space units crds),
        next `SM.notMember` sys]

route :: Space -> Units -> Coords -> Overlay -> Coords -> Overlay
route space units src sys dest = if dest == src
  then SM.insert dest [src] sys else sys' where
  sys' = snd $ minimumBy (on compare safely) [route' crds
   | crds <- next4, crds `SM.notMember` sys]
  route' crds = (crds, route space units crds sys dest)
  safely (k, xvs) = length $ xvs SM.! k
  next4 = adj space units src :: [Coords]

resolve sys k xs = resolve' xs [k] where
  resolve' (x:xs) (y:ys) = if diff x y && (length (sys SM.! x) < length (sys SM.! y))
    then resolve' xs (x:y:ys) else resolve' xs (y:ys)
  resolve' [] ys = ys

diff (a,b) (c,d) = length (nub [a,b,c,d]) < 4 && (abs $ a-c) + (abs $ b-d) == 1

damage :: Mob -> Maybe Mob -> Maybe Mob
damage agg (Just def) = if _hp def' > 0 then Just def'
  else Nothing where def' = def & hp -~ (agg ^. dmg)

turn :: Space -> Units -> Coords -> Mob -> Units
turn space units key _ = do
  let (mob, units') = (units SM.! key, SM.delete key units)
  let (targets, opts') = (slots space units' mob, moves space units [] SM.empty key)
  let alt = foldl (route space units key) SM.empty targets
  let opts = SM.mapWithKey (resolve opts') opts'
  let selected = targets `intersect` SM.keys opts
  let nearest = traceShow (alt) $ (++) (sortOn (length.(opts SM.!)) selected) [key]
  let move = (++) (opts SM.! head nearest) [key] !! 1
  let units'' = SM.insert move mob units'
  case select (enemy units mob) move of
    Just attack -> SM.alter (damage mob) attack units''
    Nothing -> units''

system :: (Space, Units) -> [Units]
system (space, units) = iterate f units where
  f xs = SM.foldlWithKey (turn space) xs xs

test = do
  (space, units) <- input
  pure $ build space units (SM.singleton (1,2) [(1,2)]) (1,3)
