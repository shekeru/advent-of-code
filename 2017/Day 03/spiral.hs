{-# LANGUAGE PartialTypeSignatures #-}
module Main where

import Text.Printf

main :: IO()
main = do
    let input = 361527
    printf "Silver: %d\n" $ part1 input
    -- printf "Gold: %d\n" $ head (filter
    --     (>input) $ concat grid)

part1 :: Int -> Int
part1 x = layer + abs offset where
  layer = ceiling $ (sqrt (fromIntegral x) -1) / 2
  offset = layer - mod (x - start) (2 * layer)
  start = (2 * layer -1) ^ 2

points :: [(Int, Int)]
points = zip (shell 1 1 0) (shell 1 0 0)

shell :: Int -> Int -> Int -> [Int]
shell tick dest prev = replicate tick prev ++ [prev,prev+y..dest-y]
  ++ shell (tick + 1) (fromEnum neg - dest) dest where
    y = if neg then (-1) else 1; neg = dest < 0
