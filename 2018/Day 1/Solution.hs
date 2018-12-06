module Main where

import Data.Set (Set, singleton, insert, member)
import Control.Monad.State
import Control.Monad
import Text.Printf

main :: IO()
main = mapM_ (input >>=) [
  printf "part 1: %d\n".sum,
  printf "part 2: %d\n".(`evalState` start).reduce.cycle]
  where start = (0, singleton 0)

input :: IO [Int]
input = map (read.filter
  ('+'/=)).lines<$>readFile "input.txt"

reduce :: [Int] -> State (Int, Set Int) Int
reduce (x:xs) = do
  (past, seen) <- get
  let count = past + x
  put (count, insert count seen)
  if member count seen then
    return count else reduce xs
