module Main where

import qualified Data.Map.Strict as Map

type Points = Map.Map (Int, Int) Int

main = print ""

yield :: Int -> Points
yield serial = foldl (apply serial) Map.empty [(x, y) | y <- [1..300], x <- [1..300]]

apply :: Int -> Points -> (Int, Int) -> Points
apply grid xvs (x,y) = Map.insert (x,y) value xvs where
  value = point + get (x-1, y) + get (x, y-1) - get (x-1, y-1)
  point = digit $ (10 + x) * (grid + (x + 10) * y)
  get k = Map.findWithDefault 0 k xvs
  digit n = mod (div n 100) 10 - 5
