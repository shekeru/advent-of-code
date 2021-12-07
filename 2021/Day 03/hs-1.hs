{-# LANGUAGE PartialTypeSignatures #-}

import Numeric (readBin)
import Text.Printf (printf)
import Data.List (sort, group, transpose)
import Control.Applicative (liftA2)

type Count = (Int, Char)
type Iter = (Int, [String])

main :: IO ()
main = input >>= liftA2
  (printf "Silver: %d\nGold: %d\n") silver gold

gold :: [String] -> Int
gold vals = product $ map (`reduce` (0, vals)) [head, last]

silver :: [String] -> Int
silver = product.map parse.transpose.map greeks.transpose

reduce :: ([Char] -> Char) -> Iter -> Int
reduce _ (_, [single]) = parse single
reduce fn (ix, vals) = reduce fn (ix + 1, filter (\xs -> coeff ==  xs !! ix) vals)
  where coeff = fn $ greeks $ (transpose $ vals) !! ix

greeks :: String -> [Char]
greeks = map snd.sort.map count.group.sort
  where count xs = (length xs, head xs)

input :: IO [[Char]]
input = lines <$> readFile "i1.txt"

parse :: String -> Int
parse = fst.head.readBin
