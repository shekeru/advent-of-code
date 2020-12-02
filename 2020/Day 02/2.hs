import Text.Printf ( printf )
import Control.Arrow

type Entry = (Int, Int, Char -> Bool, String)

input :: IO [String]
input = lines <$> readFile "input.txt"

main :: IO ()
main = mapM_ (printf *** inp >>> uncurry (=<<))
  [("first: %d\n", solve1), ("second %d\n", solve2)] where
    inp f = length.filter f.map parse <$> input

parse :: String -> Entry
parse s = (from, to, search, str) where
  (from, s') = first read $break (=='-') s
  (to, rest) = first (read.drop 1) $break (==' ') s'
  (search, str) = ((==).head.drop 1) *** drop 2 $break (==':') rest

solve1 :: Entry -> Bool
solve1 (from, to, x, xs) = count >= from && count <= to
    where count = length $ filter x xs

solve2 :: Entry -> Bool
solve2 (from, to, x, xs) = uncurry (/=) $(fn *** fn)
  (from, to) where fn = x.(!!) xs.(subtract 1)
