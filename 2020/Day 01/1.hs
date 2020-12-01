import Text.Printf
import Control.Arrow
import Data.Function
import Data.Functor

main :: IO ()
main = do
  fn <- solve <$> input
  fn 2 &printf "Silver: %d\n"
  fn 3 &printf "Gold: %d\n"

solve :: [Int] -> Int -> Int
solve xs n = snd.head.filter ((== 2020).fst)
  $mapM (const xs) [1..n] <&> (sum &&& product)

input :: IO [Int]
input = map read.lines
  <$> readFile "input.txt"
