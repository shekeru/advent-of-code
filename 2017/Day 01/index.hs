{-# LANGUAGE OverloadedStrings #-}
module Main where

import Data.String.Utils
import Text.Printf

main :: IO ()
main = do
  input <- map (read.pure).strip <$> readFile "input.txt"
  printf "Silver: %d\n" $ solve 1 input
  printf "Gold: %d\n" $ solve
    (length input `div` 2) input

solve :: Int -> [Int] -> Int
solve n xs = foldl add 0 $ pair n xs where
  add z (a, b) = z + if a == b then a else 0

pair :: Int -> [Int] -> [(Int, Int)]
pair n xs = zip xs $ (xs !!) .
  (`mod` length xs) <$> [n..]
