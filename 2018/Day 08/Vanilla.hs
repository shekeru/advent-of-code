{-#LANGUAGE PartialTypeSignatures#-}
module Main where

import Data.Function
import Text.Printf

data Tree = State Tree Counters Input
  | Node Children Meta deriving Show

type Counters = (Int, Int)
type Children = [Tree]
type Input = [Int]
type Meta = [Int]

type Solution = Int
type Length = Int

yield :: Input -> Tree
yield (a:b:xs) = eval$ State (Node [] []) (a, b) xs

eval :: Tree -> Tree
eval (State (Node kids _) (0, metas) xs) = Node (reverse kids) (take metas xs)
eval (State (Node kids _) (c, metas) (k:m:xs)) = eval$ State (Node (next:kids) []) (c-1, metas) ys
  where next = eval$ State (Node [] []) (k,m) xs; ys = drop (yielded next - 2) xs

yielded :: Tree -> Length
yielded (Node ns vs) = 2 + length vs + (sum $yielded <$>ns)

silver :: Tree -> Solution
silver (Node ns vs) = on (+) sum vs $silver <$>ns

gold :: Tree -> Solution
gold (Node [] vs) = sum vs
gold (Node ns vs) = sum [gold.last
  $take v ns | v <- vs, v <= length ns]

main :: IO ()
main = do
  tree <- yield <$> input
  printf "Silver: %d\n" $silver tree
  printf "Gold: %d\n" $gold tree

input :: IO Input
input = map read.words <$>
  readFile "input.txt"
