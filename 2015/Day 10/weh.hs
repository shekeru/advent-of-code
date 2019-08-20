{-# LANGUAGE PartialTypeSignatures #-}
module Main where

import Data.List
import Text.Printf

main :: IO()
main = do
  let input = 1113122113
  printf "Silver: %d\n" $ length
    (force input !! 40)
  printf "Gold: %d\n" $ length
    (force input !! 50)

force :: Integer -> [String]
force = iterate step.show

step :: String -> String
step = concatMap join.group where
  join xs = show (length xs) ++ [head xs]
