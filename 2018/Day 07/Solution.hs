{-#LANGUAGE PartialTypeSignatures#-}
module Main where

import qualified Data.Map.Lazy as Map
import qualified Data.Set as Set
import Control.Monad.State
import Debug.Trace
import Text.Printf
import Data.Char

type Solution = (Int, String)
type Parents = Set.Set Node
type Table = Map.Map Node Parents
type Pair = [Node]; type Node = Char

data Queue = Queue {
  limit :: Int, delay :: Maybe Int,
  elapsed :: Int, workers :: [(Char, Int)]
} deriving Show

main = do
  table <- construct<$>input
  printf "part 1: %s\n" $snd (evaluate 1 Nothing table)
  printf "part 2: %d\n" $fst (evaluate 5 (Just 60) table)

evaluate :: Int -> Maybe Int -> Table -> Solution
evaluate workers delay table = forwards `evalState` ("",
  Queue workers delay (-1) [], table)

forwards :: State ([Node], Queue, Table) Solution
forwards = do
  (accum, queue, table) <- get
  let next = nextKeys table
  let (used, ready) = pushInto queue next
  let table' = removeKeys table used
  let (done, work) = decrement ready
  let state = advanceSets table' done
  let text = accum ++ done
  put (text, work, state)
  if Map.null state && (null $workers work)
    then pure(elapsed work, text) else forwards

decrement :: Queue -> ([Node], Queue)
decrement (Queue l t e xs) = (zs, Queue l t (e+1) ys) where
  ys = [(x, time - 1) | (x, time) <- xs, time > 0]
  zs = [x | (x, time) <- xs, (time-1) < 1]

pushInto :: Queue -> [Node] -> ([Node], Queue)
pushInto start@(Queue l t e xs) ys = (zs, foldr part start zs) where
  offset y = (y, case t of Just i -> i + ord y - 64; Nothing -> 0)
  part y (Queue l t e xs) = Queue l t e $ offset y:xs
  zs = take (l - length xs) ys

removeKeys :: Table -> [Node] -> Table
removeKeys table xs = Map.withoutKeys table (Set.fromList xs)

advanceSets :: Table -> [Node] -> Table
advanceSets = foldr (Map.map .Set.delete)

nextKeys :: Table -> [Node]
nextKeys table = fst$ Map.mapAccumRWithKey func "" table
  where func prev key list = (if Set.null list then key:prev else prev, list)

construct :: [Pair] -> Table
construct = foldr part (Map.fromSet (const Set.empty) $Set.fromAscList ['A'..'Z']) where
  part [req, key] = Map.insertWith Set.union key (Set.singleton req)

input :: IO [Pair]
input = map (tail.parse).lines<$>readFile "input.txt"
  where parse = filter (`elem` ['A'..'Z'])
