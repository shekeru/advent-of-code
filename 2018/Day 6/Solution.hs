{-#LANGUAGE PartialTypeSignatures#-}
module Solution where

import Data.List.Split
import Control.Monad
import Data.Function
import Text.Printf
import Data.List

type Coords = (Int, Int)

--main :: IO()
main = print ""

input :: IO [Coords]
input = map (pair.parse).lines<$>readFile "input.txt"
  where pair [a,b] = (a,b); parse = map read.splitOn ","

enclosed points = maximum.assemble'$ do
  ys <- range snd points; xs <- range fst points
  let table = distance' (xs, ys) <$> points
  let opt = minimumBy (on compare fst) table
  guard (length (filter (on (==) fst opt) table) == 1)
  return $ snd opt

assemble :: Eq a => [a] -> [(a, Int)]
assemble xs = count xs <$> xs where
  count xs x = (x, length $filter (== x) xs)

assemble' :: Eq a => [a] -> [Int]
assemble' xs = count xs <$> xs where
  count xs x = length $filter (== x) xs

test :: [Coords]
test = [
  (1, 1),
  (1, 6),
  (8, 3),
  (3, 4),
  (5, 5),
  (8, 9)]


adjacent :: [Coords] -> Int
adjacent points = length [1 |
  ys <- range snd points, xs <- range fst points,
  (sum $distance (xs, ys) <$> points) < 10000]

distance :: Coords -> Coords -> Int
distance (x1,y1) (x,y) = on (+) abs (x1-x) (y1-y)

distance' :: Coords -> Coords -> (Int, Coords)
distance' (x1,y1) l@(x,y) = (on (+) abs (x1-x) (y1-y), l)

range :: (Coords -> Int) -> [Coords] -> [Int]
range f xs = [minimum ys..maximum ys-1]
  where ys = map f xs
