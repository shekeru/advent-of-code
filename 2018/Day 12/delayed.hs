{-# LANGUAGE PartialTypeSignatures #-}
module Main where

import qualified Data.IntMap.Strict as SM
import qualified Data.Map.Strict as LM
import qualified Data.IntSet as SI
import Data.List.Split (splitOn)
import Text.Printf (printf)

type Trans = LM.Map [Plant] Plant
type State = SM.IntMap Plant
type Plant = Char

main :: IO ()
main = do
  system <- map solve.states<$>input
  printf "Silver: %d\n" $system !! 20
  printf "Gold: %d\n" $stabs system 50000000000

input :: IO (Trans, State)
input = parse.lines<$>readFile "input.txt"

parse :: [String] -> (Trans, State)
parse (x:_:xs) = (LM.fromList ejects, SM.fromAscList state) where
  state = (zip [0..].last.splitOn ": ") x; swap [ys, y:_] = (ys, y)
  ejects = map (swap.splitOn " => ") xs

stabs :: [Int] -> Int -> Int
stabs (a:b:c:xs) i = if (b - a) == (c - b)
  then a + (c - b) * i else stabs xs (i - 3)

states :: (Trans, State) -> [State]
states (ts, st) = iterate (runSystem ts) st

runSystem :: Trans -> State -> State
runSystem trans x = SM.foldlWithKey (stepSystem trans x)
  SM.empty (statePad $collect x)

stepSystem :: Trans -> State -> State -> SM.Key -> Plant -> State
stepSystem trans xs ys k a = SM.insert k a' ys where
  kts = map (\k -> SM.findWithDefault '.' k xs) [k-2..k+2]
  a' = LM.findWithDefault a kts trans

statePad :: State -> State
statePad xs = foldl pads xs (mins ++ maxs) where
  [(u, u'), (v, v')] = [SM.findMin, SM.findMax] <*> [xs]
  limit ['.', '#'] = take 1; limit ['#', _] = take 2
  limit _ = take 0; pads xs k = SM.insert k '.' xs
  maxs = limit [v', xs SM.! (v-1)] [v+1, v+2]
  mins = limit [u', xs SM.! (u+1)] [u-1, u-2]

collect :: State -> State
collect xs = SM.restrictKeys xs $ SI.fromList [u..v] where
  [(u, u'), (v, v')] = [SM.findMin, SM.findMax] <*> [active xs]

active :: State -> State
active = SM.filter ('#' ==)

solve :: State -> Int
solve = sum.SM.keys.active
