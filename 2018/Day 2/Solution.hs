module Solution where

import Control.Monad
import Text.Printf
import Data.List

main :: IO()
main = mapM_ (input >>=) [
  printf "part 1: %d\n".checkSum,
  printf "part 2: %s\n".head.concatMap
    match.iterate tail]

input :: IO [String]
input = lines<$>readFile "input.txt"

count :: Eq a => [a] -> [a] -> [Int]
count elems list = map (($list).count') elems
  where count' y = length.filter (y ==)

checkSum :: Foldable t => t String -> Int
checkSum = product.count [2,3].concatMap
  (intersect [2,3].count ['a'..'z'])

match :: Eq t => [[t]] -> [[t]]
match (current:list) = do
    option <- charXor current<$>list
    let check = length option + 1 == length current
    guard check; return option

charXor :: Eq t => [t] -> [t] -> [t]
charXor xs ys = [x | (x,y) <- zip xs ys, x == y]
