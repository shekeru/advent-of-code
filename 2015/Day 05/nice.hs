module Main where

import Data.List
import Text.Printf

main :: IO ()
main = do
  ln <- lines <$> readFile "input.txt"
  printf "Silver: %d\n" $ length (filter isNice ln)
  printf "Gold: %d\n" $ length (filter isNicer ln)
-- Part Two
isNicer :: String -> Bool
isNicer xs = check (pair xs) && mid xs

check :: [String] -> Bool
check (x:y:z) = x `elem` z || check (y:z)
check _ = False

mid :: String -> Bool
mid (a:b:c:xs) = a == c || mid (b:c:xs)
mid _ = False
-- Part One
isNice :: String -> Bool
isNice str = and $ [three, twice, nice] <*> [str] where
  nice = all (`notElem` ["ab", "cd", "pq", "xy"]).pair
  three = (>= 3).length.filter isVowel
  twice = any ((>= 2).length).group
-- Helper Functions
isVowel :: Char -> Bool
isVowel = flip elem "aeiou"

pair :: String -> [String]
pair (x:y:z) = [x,y] : pair (y:z)
pair _ = []
