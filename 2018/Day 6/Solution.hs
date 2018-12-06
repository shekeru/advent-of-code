module Solution where

import Data.Function
import Text.Printf
import Data.Char

main :: IO()
main = print ""

input :: IO String
input = init<$>readFile "input.txt"

reduction :: Char -> String -> String
reduction x ys = if reacts x $head ys then ys else x:ys
  where reacts x y = x /= y && on (==) toLower x y

swaps :: String -> [String]
swaps xs = map strip ['a'..'z'] <*> [xs] where
  strip x = filter (`notElem` [x, toUpper x])
-- Yay, Learning
swaps' :: String -> [String]
swaps' str = strip' str <$> ['a'..'z']
strip' :: String -> Char -> String
strip' str x = filter ((x /=).toLower) str
swaps'' :: String -> [String]
swaps'' = flip (<$>) ['a'..'z'] .strip'
