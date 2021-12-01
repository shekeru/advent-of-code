{-# LANGUAGE ViewPatterns #-}

import Data.List
import Text.Printf
import Control.Applicative
import Data.Function

type Window = [Int]

main :: IO ()
main = map read.lines <$> readFile "i1.txt" >>= liftA2
  (printf "Silver: %d\nGold: %d\n" `on` solve) (map pure) (window 3)


solve :: [Window] -> Int
solve = foldl (\v [a, b] -> v + fromEnum (a < b)) 0.window 2.map sum

window :: Int -> [Int] -> [Window]
window ((-1+) -> k) xs = take (length xs - k)
  $ transpose $ [ drop j xs | j <- [0..k]]
