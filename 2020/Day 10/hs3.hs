import Text.Printf
import Data.List

main :: IO ()
main = do
  convs <- sort.map read.lines <$> readFile "input.txt"
  let array = zipWith subtract <*> tail $0 :convs <> [last convs + 3]
  printf "Silver: %d\n" $product [length x | x <- group $sort $array]
  printf "Gold: %d\n" $product [swaps $sum x | x <- group array, elem 1 x]
    where swaps 0 = 1; swaps v = sum [swaps $v-o | o <- [1..3], v >= o] :: Int
