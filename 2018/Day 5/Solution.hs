{-#LANGUAGE PartialTypeSignatures#-}
module Solution where

import Data.Function
import Text.Printf
import Data.Char

main :: IO()
main = mapM_ (input >>=) [
   printf "part 1: %d\n".solve,
   printf "part 2: %d\n".minimum.map solve.swaps]
    where solve = length.foldr reduction ""

input :: IO String
input = init<$>readFile "input.txt"

reduction :: Char -> String -> String
reduction x [] = [x]
reduction x zs@(y:ys) = if reacts x y then ys else x:zs
  where reacts x y = x /= y && on (==) toLower x y

swaps :: String -> [String]
swaps xs = map strip ['a'..'z'] <*> [xs] where
  strip x = filter $not.flip elem [x, toUpper x]
