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

main :: IO ()
main = do
  xs <- system <$> input
  print $ head xs

input :: IO (Map, [Coords])
input = parse.map regex.lines <$> readFile "test.txt" where
  regex xs = (head xs, map read $ matches $xs *=~ [re|@{%int}|])
  parse xs = (foldl expand SM.empty xs, [(1, 500)]) where
    expand vs ('y', [y,a,b]) = foldl (\vs x -> SM.insert (y, x) Clay vs) vs [a..b]
    expand vs ('x', [x,a,b]) = foldl (\vs y -> SM.insert (y, x) Clay vs) vs [a..b]

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

varFill :: Map -> Coords -> Int -> [Coords]
varFill vs k@(y, x) i = if fill_check (y+1, x) && (! fill_check k)
    then k : varFill vs (y, x - i) i else [] where
      checking z = solid $ safelyGet z vs

system :: (Map, [Coords]) -> [(Map, [Coords])]
system = iterate physics

physics :: (Map, [Coords]) -> (Map, [Coords])
physics (state, starts) = do
  let (state', flows) = foldl flow (state, []) starts
  let next = foldl expand state' flows
--foldl spill (next, []) keys

safelyGet :: Coords -> Map -> Tile
safelyGet = SM.findWithDefault Empty

valid :: Map -> Coords -> Bool
valid vs (y,x) = (fst.fst.SM.findMax) vs >= y

solid :: Tile -> Bool
solid tile = tile == Water || tile == Clay
