{-# LANGUAGE QuasiQuotes #-}

import Text.Printf
import Data.Hashable
import Text.RE.TDFA.String
import Data.Function
import Data.List

type Body = ([Int], [Int])

main :: IO()
main = do
  pts <- iterate (map step.update) <$> input
  let (zero: rest) = map state pts
  let factors = zip zero $transpose rest
  printf "Silver: %d\n" $energy pts 1000
  printf "Gold: %d\n" $foldl (\a e -> lcm a $e +1)
    1 $map (head.uncurry elemIndices) factors

state :: [Body] -> [Int]
state = map hash.transpose.map
  (map hash.uncurry zip)

energy :: [[Body]] -> Int -> Int
energy xs = sum.map fn.(xs!!) where
  fn = uncurry(on (*)$ sum.map abs)

step :: Body -> Body
step (p, v) = (zipWith (+) p v, v)

update :: [Body] -> [Body]
update = flip(foldl force) >>= map

force :: Body -> Body -> Body
force (p, v) (o, _) = (p, zipWith (+) v $subtract
  1.fromEnum.uncurry compare <$> zip o p)

input :: IO [Body]
input = merge.regex.lines <$> readFile "ins.txt" where
  regex = map $map read.matches.(*=~ [re|@{%int}|])
  merge xs = xs `zip` repeat [0, 0, 0]
