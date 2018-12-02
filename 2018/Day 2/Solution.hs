module Solution where

main = print ""

input :: IO [String]
input = lines<$>readFile "input.txt"
