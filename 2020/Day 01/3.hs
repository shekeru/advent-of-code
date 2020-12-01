import Text.Printf
import Data.Function
import Data.Functor
import Data.List

main :: IO ()
main = do
  fn <- solve <$> input
  fn 2 &printf "Silver: %d\n"
  fn 3 &printf "Gold: %d\n"

solve :: [Int] -> Int -> Int
solve = fn <&> fmap(snd.head.filter ((== 2020).fst).map (\v -> (sum v, product v)))
  where fn xs 0 = [[]]; fn xs n = [y:ys | y:xs' <- tails xs, ys <- fn xs' $n -1]

input :: IO [Int]
input = map read.lines <$> readFile "input.txt"
