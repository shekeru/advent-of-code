module Main where

main :: IO ()
main = do
  input <- head.lines<$>readFile "input.txt"
  let floors = scanl (\x y -> if y == ')' then x-1 else x+1) 0 input
  putStrLn$ "Silver: "++ (show $last floors); putStrLn$
    "Gold: "++ (show $length $takeWhile (-1 /=) floors)
