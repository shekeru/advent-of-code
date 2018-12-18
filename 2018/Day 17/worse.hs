{-#LANGUAGE PartialTypeSignatures, QuasiQuotes#-}
module Main where

import qualified Data.Map.Strict as SM
import Text.RE.TDFA.String
import Data.List.Split

type Map = SM.Map Coords Tile
data Tile = Clay | Empty | Flowing | Water
  deriving (Show, Eq)
type Vein = (Char, [Int])
type Coords = (Int, Int)

main = print ""

input :: IO (Map, [Coords])
input = parse.map regex.lines <$> readFile "input.txt" where
  regex xs = (head xs, map read $ matches $xs *=~ [re|@{%int}|])
  parse xs = (foldl handle (SM.singleton (1, 500) Flowing) xs, [(1, 500)])

handle :: Map -> Vein -> Map
handle vs ('y', [y,a,b]) = foldl (\vs x -> SM.insert (y, x) Clay vs) vs [a..b]
handle vs ('x', [x,a,b]) = foldl (\vs y -> SM.insert (y, x) Clay vs) vs [a..b]

safelyGet :: Coords -> Map -> Tile
safelyGet = SM.findWithDefault Empty

flow :: (Map, [Coords]) -> Coords -> (Map, [Coords])
flow (vs, keys) k@(y, x) = case safelyGet k vs of
  Empty -> if valid vs k then flow (SM.insert k Flowing vs, k:keys)
    (y+1, x) else (vs, keys); Flowing -> flow (vs, keys) (y+1,x);
    Clay -> (vs, keys); Water -> (vs, keys)

sides :: Map -> Coords -> Map
sides vs k@(y,x) = if solid below && not (solid pos) &&
  (solid left || solid right) then foldl sides
    vs' [(y, x+1), (y, x-1)] else vs where
    right = safelyGet (y, x+1) vs; left = safelyGet (y, x-1) vs
    below = safelyGet (y+1, x) vs; pos = safelyGet k vs
    vs' = SM.insert k Water vs

spill :: (Map, [Coords]) -> Coords -> (Map, [Coords])
spill (vs, keys) k@(y, x) = if ((pos == Flowing && not adj) || (adj && pos /= Flowing))
  && solid below then foldl spill (vs', k:keys) [(y, x+1), (y, x-1)] else extend (vs, keys) where
    vs' = SM.insert k Flowing vs; adj = left == Flowing || right == Flowing
    right = safelyGet (y, x+1) vs; left = safelyGet (y, x-1) vs
    below = safelyGet (y+1, x) vs; pos = safelyGet k vs

extend :: (Map, [Coords]) -> (Map, [Coords])
extend (vs, keys) = foldl addFlow (vs, keys) opts' where
  addFlow cmb (y,x) = foldl (\(vs, keys) k -> (SM.insertWith seq k Flowing vs, k:keys))
    cmb [(y, x+1), (y, x-1)]; opts' = SM.keys$ SM.filterWithKey (\
      (y, x) a -> Flowing == a && (solid $ safelyGet (y+1, x) vs)) vs

valid :: Map -> Coords -> Bool
valid vs (y,x) = (fst.fst.SM.findMax) vs >= y

solid :: Tile -> Bool
solid tile = tile == Water || tile == Clay

physics :: (Map, [Coords]) -> (Map, [Coords])
physics (state, starts) = do
  let (two, keys) = foldl flow (state, []) starts
  let next = foldl sides two keys
  foldl spill (next, []) keys

system :: (Map, [Coords]) -> [(Map, [Coords])]
system = iterate physics
