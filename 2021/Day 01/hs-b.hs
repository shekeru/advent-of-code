{-# LANGUAGE ViewPatterns #-}

import Data.List
import Text.Printf
import Data.Function

type Window = [Int]

main :: IO ()
main = (map sum.window 3 >>= flip
  (printf "Silver: %d\nGold: %d\n" `on` solve))
  =<< map read.lines <$> readFile "i1.txt"

solve :: [Int] -> Int
solve = foldl (\v [a, b] -> v + fromEnum (a < b)) 0.window 2

window :: Int -> [Int] -> [Window]
window ((-1+) -> k) xs = take (length xs - k)
 $ transpose $ map (`drop` xs) [0..k]
