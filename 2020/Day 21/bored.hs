{-# LANGUAGE ViewPatterns #-}

import Control.Arrow
import Data.List.Split
import Data.Function
import Text.Printf
import Data.List

main :: IO ()
main = do
  (rules, opts) <- ((,) <*> merge) <$> readF "input.txt"
  rules >>= snd &printf "Silver: %d\n".length.filter (`notElem`
    (nub $opts >>= snd)); solve [] opts &printf "Gold: %s\n"

solve :: [Pair] -> [Assoc] -> String
solve ys [] = intercalate "," $map snd $sortOn fst ys
solve ys xs = solve ((a, i):ys) $map (second $delete i) $filter
  ((/= a).fst) xs where Just (a, [i]) = find ((== 1).length.snd) xs

merge :: [Line] -> [Assoc]
merge xss = map fn $nub $concatMap fst xss where
  fn i = (i, foldl1 intersect $map snd
    $filter (any (== i).fst) xss)

readF :: String -> IO [Line]
readF wh = map (fn.splitOn " (contains ").lines <$> readFile
  wh where fn [words -> i, init -> a] = (splitOn ", " a, i)

type Assoc = (String, [String])
type Line = ([String], [String])
type Pair = (String, String)
