{-# LANGUAGE PartialTypeSignatures, ViewPatterns #-}
module Main where

import qualified Data.Sequence as S
import Data.Char (digitToInt)
import Data.Digits (digits)

type State = (Series, Int, Int)
type Series = S.Seq Int

main :: IO ()
main = do
  let subseq = map digitToInt input; input = "030121"
  let (_, nums) = (head.filter fst.map (match subseq 7)) sets
  putStrLn $ "Silver: " ++ concatMap show (S.take 10 $ S.drop
    (read input) nums); putStrLn $ "Gold: " ++ (show.length) nums

sets :: [State]
sets = iterate next (S.fromList [3,7], 1, 0)

next :: State -> State
next (xs, u, v) = (xs', f' u, f' v) where
  xs' = foldl (S.|>) xs (if null ys then [0] else ys)
  f' j = mod (j + 1 + ret j) $length xs'
  ys = digits 10 (ret u + ret v)
  ret = S.index xs

match :: [Int] -> Int -> State -> (Bool, Series)
match str i (S.viewr -> S.EmptyR, u, v) = (False, S.empty)
match str i (S.viewr -> xs S.:> x, u, v)
  | last (-1:str) == x = match (init str) (i-1) (xs, u, v)
  |  i > 6 = match str (i-1) (xs, u, v)
  | otherwise = (null str, xs S.|> x)
