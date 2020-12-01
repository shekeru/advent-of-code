import Text.Printf
import Control.Arrow
import Data.Function
import Data.Functor
import Data.List

main :: IO ()
main = do
  fn <- fmap solve input
  fn 2 &printf "Silver: %d\n"
  fn 3 &printf "Gold: %d\n"

solve :: [Int] -> Int -> Int
solve = ($).fn <&> (.) (snd.head.filter ((== 2020).fst).fmap (sum &&& product))
  where fn xs 0 = [[]]; fn xs n = [y:ys | y:xs' <- tails xs, ys <- n -1 &fn xs']

input :: IO [Int]
input = map read.lines <$> readFile "input.txt"
