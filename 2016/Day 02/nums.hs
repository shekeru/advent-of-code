{-# LANGUAGE LambdaCase #-}
module Main where

import Text.Printf
import Data.Char
import Numeric

main :: IO ()
main = do
    ln <- lines <$> 
        readFile "input.txt"
    printf "Silver: %s\n" $ 
        concatMap part1 ln
    printf "Gold: %s\n" $ 
        concatMap part2 ln

part1 :: String -> String
part1 = number.foldl (grid 1) [0,0] where
    number [x, y] = show $ x + 5 - (3 * y)

part2 :: String -> String
part2 = number.foldl grid' [0,0] where
    number [x, y] = map toUpper.($ "").showHex $ x + 7 - y' 
        where y' = max (min 1 y) (-1) * [0, 4, 6] !! abs y 
    grid' old = limit.grid 2 old where limit new = if 
        sum (abs <$> new) > 2 then old else new 
    
grid :: Int -> [Int] -> Char -> [Int]
grid t [x,y] = \case
    'R' -> [min t $ x + 1, y]
    'L' -> [max (-t) $ x - 1, y]
    'D' -> [x, max (-t) $ y - 1]
    'U' -> [x, min t $ y + 1]
