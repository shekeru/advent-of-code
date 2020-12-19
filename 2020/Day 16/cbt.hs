{-# LANGUAGE ViewPatterns #-}

import Text.Printf
import Control.Arrow
import Control.Applicative
import Data.List.Split
import Data.List

main :: IO ()
main = do
  (fields, (your : tickets)) <- input
  let (silver, product.map ((your !!).snd).filter (elem "departure".words.fst).relate
        .compile fields.map snd.filter fst -> gold) = mapAccumL (verify fields) 0 tickets
  printf "Silver: %d\nGold: %d\n" silver gold
type Field = (String, Int -> Bool)

relate :: [(Int, [String])] -> [(String, Int)]
relate ((i, [r]):xs) = (r, i) : relate
  (second (delete r) <$> xs); relate _ = []

compile :: [Field] -> [Ticket] -> [(Int, [String])]
compile fxs txs = sortOn (length.snd) [(j, [fr | (fr, fn)
  <- fxs, all (fn.(!! j)) txs]) | j <- [0..length (head txs) - 1]]

verify :: [Field] -> Int -> Ticket -> (Int, (Bool, Ticket))
verify fxs acc xs = (acc + sum wrong, (null wrong, xs))
  where wrong = filter (not.or.sequence (map snd fxs)) xs

input :: IO ([Field], [Ticket]); type Ticket = [Int]
input = fn.splitOn [""].lines <$> readFile "input.txt" where
  fn [hd, last -> yr, tail -> ot] = (map (fuck.splitOn ":") hd, map (map read.splitOn ",") $yr:ot)
  fuck [tag, splitOn "or" -> body] = (tag, \x -> any (($x).shit.map read.splitOn "-") body)
  shit [a, b] = liftA2 (&&) (a <=) (<= b)
