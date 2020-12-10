import Text.Printf
import Data.List

main :: IO ()
main = do
  array <- sort.map read.lines <$> readFile "input.txt"
  printf "Silver %d\n" $silver $0 :array <> [last array + 3]
  printf "Gold: %d\n" $gold array [(0, 1)]

silver :: [Int] -> Int
silver = product.map length.group.sort.(zipWith subtract <*> tail)

gold :: [Int] -> [(Int, Int)] -> Int
gold [] vs = snd $head $vs; gold (k:xs) sums = gold xs $(k, total):sums where
  total = foldr (\(_, t) -> (+t)) 0 $takeWhile (\(v, _) -> k - v <= 3) sums
