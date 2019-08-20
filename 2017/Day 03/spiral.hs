{-# LANGUAGE PartialTypeSignatures #-}
module Main where

import Data.Function
import Control.Monad
import Text.Printf
import Data.Map

type Spiral = Map Coords Int
type Coords = (Int, Int)

main :: IO()
main = do
    let input = 361527
    printf "Silver: %d\n"
      $ part1 input
    printf "Gold: %d\n"
      $ part2 input

part2 :: Int -> Int
part2 x = head $ dropWhile (< x) spiral

part1 :: Int -> Int
part1 x = layer + abs offset where
  layer = ceiling $ (sqrt (fromIntegral x) -1) / 2
  offset = layer - mod (x - start) (2 * layer)
  start = (2 * layer -1) ^ 2

spiral :: [Int]
spiral = maximum.elems <$> scanl reduce
  (singleton (0,0) 1) (nby <$> points)

reduce :: Spiral -> [Coords] -> Spiral
reduce z xs = insert (xs !! 4) (sum $ ins <$> xs) z
  where ins k = findWithDefault 0 k z

nby :: Coords -> [Coords]
nby = uncurry $ on (liftM2 (,)) go
  where go n = [n-1..n+1]

points :: [Coords]
points = tail $ zip
  (shell 1 1 0) (shell 0 1 0)

shell :: Int -> Int -> Int -> [Int]
shell tick dest prev = replicate tick prev ++ [prev,prev+y..dest-y]
  ++ shell (tick + 1) (fromEnum neg - dest) dest where
    y = if neg then (-1) else 1; neg = dest < 0
