import Control.Arrow (first, second)
import qualified Data.Vector as V
import Control.Monad (guard)
import Text.Printf (printf)
import Data.List (tails)


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
  let sums = map sum $combination zone 2
  guard (notElem v sums) >> pure v

part2 :: (Bins, Int) -> (Int, Int) -> Int
part2 (xs, v) p@(a, b) = if v == piss then minimum
  shit + maximum shit else part2 (xs, v) (fuck p) where
  fuck = (if piss > v then first else second) (+1)
  shit = V.slice a (b - a) xs; piss = sum shit

combination :: [a] -> Int -> [[a]]
combination xs 0 = pure mempty
combination xs n = do
  (y:xs') <- tails xs
  ys <- combination xs' (n-1)
  return (y:ys)

input :: IO Bins
input = V.fromList.map read.lines
  <$> readFile "input.txt"
