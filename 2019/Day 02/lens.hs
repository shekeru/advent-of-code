{-#LANGUAGE QuasiQuotes #-}
module Lens where

import Data.Function
import Control.Lens hiding (re)
import Text.RE.TDFA.String
import Text.Printf

main :: IO()
main = do
  xs <- input
  let (n, v) = (12, 2)
  printf "Silver: %d\n"
    $ eval xs n v
  printf "Gold: %d\n"
    $ settle xs n v

settle :: [Int] -> Int -> Int -> Int
settle xs n v = 100 * n' + v' where
  rvs fn x = head (filter fn [x..]) - 1
  v' = rvs (\v -> t < eval xs n' v) v
  n' = rvs (\n -> t < eval xs n 2) n
  t = 19690720

eval :: [Int] -> Int -> Int -> Int
eval arr n v = run 0 (arr & ix 1 .~ n & ix 2 .~ v) where
  run k xs = case xs !! k of
    99 -> head xs; 2 -> op (*); 1 -> op (+); where
      op fn = run (k + 4) (xs & ix c .~ on fn (xs!!) a b)
      [a, b, c] = take 3 $ drop (k + 1) xs

input :: IO [Int]
input = regex <$> readFile "input.txt" where
  regex = map read.matches.(*=~ [re|@{%int}|])
