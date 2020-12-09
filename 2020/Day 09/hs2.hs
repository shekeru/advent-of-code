import Control.Arrow (first, second)
import qualified Data.Vector as V
import Control.Monad (guard)
import Text.Printf (printf)
import Data.List (delete)

main :: IO ()
main = do
  arr <- input; let value = part1 arr
  printf "Silver: %d\n" value; printf
    "Gold: %d\n" $part2 (arr, value) (0, 1)
type Bins = V.Vector Int

part1 :: Bins ->  Int
part1 xs = head $do
  k <- [25..length xs - 1]
  let v = V.head (V.slice k 1 xs)
  let zone = V.toList $V.slice (k - 25) 25 xs
  guard (notsum zone v) >> pure v where
    notsum xs k = null [x | x <- xs,
      k - x `elem` delete k xs]

part2 :: (Bins, Int) -> (Int, Int) -> Int
part2 (xs, v) p@(a, b) = if v == piss then minimum
  shit + maximum shit else part2 (xs, v) (fuck p) where
  fuck = (if piss > v then first else second) (+1)
  shit = V.slice a (b - a) xs; piss = sum shit

input :: IO Bins
input = V.fromList.map read.lines
  <$> readFile "input.txt"
