{-#LANGUAGE QuasiQuotes, FlexibleInstances #-}
module Main where

import Text.Printf
import Text.RE.TDFA.String
import Control.Arrow
import Control.Applicative
import Control.Lens hiding (re)
import qualified Data.Map.Strict as SM
import Data.Traversable
import Data.List.Split
import Data.Function
import Data.List
import Data.Ix

type Stack = [Coords]
type Coords = (Int, Int)
data Tile = Water | Stable | Clay deriving (Eq)
type World = (SM.Map Coords Tile, ([Int], [Int]))


instance {-# OVERLAPS #-} Show World where
  show (dict, (ys, xs)) = intercalate "\n" $ chunksOf
    (length xs) $do y <- ys; x <- xs; show $ dict ^. at (y, x)

instance {-# OVERLAPS #-} Show (Maybe Tile) where
  show (Just x) = show x
  show Nothing = "."

instance Show Tile where
  show Water = "|"
  show Stable = "~"
  show Clay = "#"

main :: IO ()
main = do
  let source = [(0, 500)]
  test <- parse "test.txt" <&> flows source
  putStrLn $if 57 == solve [Water, Stable] test
    then " [Test] Okay" else " [Test] Failed"
  world <- parse "input.txt" <&> flows source
  solve [Water, Stable] world& printf "Silver: %d\n"
  solve [Stable] world& printf "Gold: %d\n"
  writeFile "what.txt" $ show world

solve :: [Tile] -> World  -> Int
solve ts = length.SM.filter (`elem` ts).fst

flows :: Stack -> World -> World
flows (x:xs) wh = wh& flows xs.spill down
  .waterify down where down = wh& reverse.flow x
flows [] wh = wh

spill :: Stack -> World -> World
spill (x:xs) wh = settle level wh& spill xs.if fst x > 0 then
  flows $map (&ix 0 -~ 1) level else id where level = expand x wh
spill [] wh = wh

waterify :: Stack -> World -> World
waterify stack (w, b) = (foldl fn w stack, b) where
  fn dict key = SM.insertWith (flip const) key Water dict

settle :: Stack -> World -> World
settle stack (w, b) = if on (-) length stack water > 1
  then (foldl fn w water, b) else (w, b) where
    water = filter (\x -> w ^. at x & solid & not) stack
    fn dict key = SM.insert key Stable dict

flow :: Coords -> World -> Stack
flow (y, x) i@(w, b@(ys, xs)) = if SM.notMember p w && y
  < maximum ys then p :flow p i else [] where p = (y+1, x)

expand :: Coords -> World -> Stack
expand pos mch = concatMap (sflow pos mch) [-1, 1]
sflow :: Coords -> World -> Int -> Stack
sflow (y, x) m@(w, b) dt = if (w ^.at(y + 1, x) &solid) && not
  (w ^.at(y, x) &solid) then (y, x) :sflow (y, x - dt) m dt else [(y, x)]

solid :: Maybe Tile -> Bool
solid (Just Water) = False
solid Nothing = False
solid _ = True

parse :: String -> IO World
parse = readFile <&> (bounded.foldl expand SM.empty.map
  (head &&& map read.matches.(*=~ [re|@{%int}|])).lines <$>) where
    expand dict (t, [k,a,b]) = foldl (\vs i -> SM.insert (fn t i) Clay vs)
      dict [a..b] where fn 'y' v = (k, v); fn 'x' v = (v, k)
    bounded = id &&& (fn *** fn).unzip.SM.keys
      where fn = range.(minimum &&& maximum)
