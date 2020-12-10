import Data.List (delete)
import Data.List.Split (divvy)
import Text.Printf (printf)

main :: IO ()
main = do
  arr <- map read.lines <$> readFile "input.txt"; printf
    "Silver: %d\nGold: %d\n" <*> part2 arr $part1 arr

part1 :: [Int] -> Int
part1 xs = head [k | (k, sp) <- zip (drop 25 xs) (zone xs),
  null $filter (\x -> k - x `elem` delete k sp) sp] where
    zone xs = take 25 xs :(zone $tail xs)

part2 :: [Int] -> Int -> Int
part2 xs k = head [minimum ys + maximum ys |
  w <- [2..], ys <- divvy w 1 xs, sum ys == k]
