{-# LANGUAGE TemplateHaskell #-}
module Main where

import Text.Printf
import Data.String.Utils
import Data.HashMap.Strict hiding (foldr)
import Control.Lens.TH
import Control.Lens

data Counter = Counter {
  _x :: Int, _y :: Int,
  _grid :: HashMap (Int, Int) Int
} deriving Show
$(makeLenses ''Counter)

main :: IO ()
main = do
  ln <- strip <$> readFile "input.txt"
  printf "Silver: %d\n" (length $ solve ln ^. grid)
  printf "Gold: %d\n".length.unions $ (^. grid).solve
    <$> foldr (\v ~[x, y] -> [v:y, x]) [[],[]] ln

solve :: String -> Counter
solve = foldl (\c -> house . step c)
  (Counter 0 0 $ singleton (0, 0) 1)

house :: Counter -> Counter
house st = grid %~ insertWith
  (+) (_x st, _y st) 1 $ st

step :: Counter -> Char -> Counter
step st i = st & case i of
  '^' -> y +~ 1; 'v' -> y -~ 1
  '>' -> x +~ 1; '<' -> x -~ 1
