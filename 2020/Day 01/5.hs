import Text.Printf
import Control.Arrow
import Data.Function
import Data.List

main :: IO ()
main = do
  fn <- fmap solve input
  fn 2 &printf "Silver: %d\n"
  fn 3 &printf "Gold: %d\n"

solve :: [Int] -> Int -> Int
solve = fn >>> fmap solve' where
  solve' = map (sum &&& product) >>> filter ((== 2020).fst) >>> head >>> snd
  fn xs 0 = [[]]; fn xs n = [y:ys | y:xs' <- tails xs, ys <- fn xs' $n -1]

input :: IO [Int]
input = map read.lines <$> readFile "input.txt"
