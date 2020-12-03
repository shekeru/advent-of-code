{-# LANGUAGE TupleSections #-}
import Text.Printf
import Data.Maybe
import Data.List

main :: IO ()
main = do
  let slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
  trees <- sequence (solve <$> slopes) <$> input
  printf "Silver: %d\n" $trees !!1
  printf "Gold: %d\n" $product trees

solve :: (Int, Int) -> [[Int]] -> Int
solve (x, y) ln = sum $uncurry (!!)
  <$> zip (every y ln) [0, x..]

every :: Int -> [a] -> [a]
every n = unfoldr$ \xs-> fmap
  (, drop n xs) (listToMaybe xs)

input :: IO [[Int]]
input = map (cycle.map (fromEnum.(== '#')))
  .lines <$> readFile "input.txt"
