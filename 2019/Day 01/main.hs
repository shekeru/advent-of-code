module Main where
import Text.Printf

main :: IO()
main = do
  ys <- total <$> input
  printf "Silver: %d\n"
    (head ys)
  printf "Gold: %d\n"
    (sum $ takeWhile (> 0) ys)

input :: IO [Int]
input = map read.lines
  <$> readFile "input.txt"

total :: [Int] -> [Int]
total = map sum . tail
  . iterate (map fuel)

fuel :: Int -> Int
fuel x = max 0 $
  x `div` 3 - 2
