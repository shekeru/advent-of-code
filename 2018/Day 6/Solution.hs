{-#LANGUAGE PartialTypeSignatures#-}
module Solution where

import Data.List.Split
import Control.Monad
import Data.Function
import Text.Printf
import Data.List

type Coords = (Int, Int)

main :: IO()
main = mapM_ (input >>=) [
   printf "part 1: %d\n".enclosed,
   printf "part 2: %d\n".adjacent]

input :: IO [Coords]
input = map (pair.parse).lines<$>readFile "input.txt"
  where pair [a,b] = (a,b); parse = map read.splitOn ","

enclosed :: [Coords] -> Int
enclosed points = maximum.assemble'$ do
  ys <- range snd points; xs <- range fst points
  let table = distance' (xs, ys) <$> points
  let (val, key) = minimumBy (on compare fst) table
  guard (count (map fst table) val == 1)
  return key

adjacent :: [Coords] -> Int
adjacent points = length [1 |
  ys <- range snd points, xs <- range fst points,
  (sum $distance (xs, ys) <$> points) < 10000]

distance :: Coords -> Coords -> Int
distance (x1,y1) (x,y) = on (+) abs (x1-x) (y1-y)

distance' :: Coords -> Coords -> (Int, Coords)
distance' a b = (distance a b, b)

assemble' :: Eq a => [a] -> [Int]
assemble' xs = count xs <$> nub xs

range :: (Coords -> Int) -> [Coords] -> [Int]
range f xs = [minimum ys..maximum ys-1]
  where ys = map f xs

count :: Eq a => [a] -> a -> Int
count xs x = length $filter (== x) xs
