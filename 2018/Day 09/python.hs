module Main where

import qualified Data.IntMap.Strict as Map
import Deque

type GameState = (Int, Map.IntMap Int, Circular)
type Circular = Deque Int

main :: IO()
main = solve 428 72061

solve :: Int -> Int -> IO()
solve players high = do
  let (k, scores, ys) = foldl applyMarble (players, Map.empty, fromList [0]) [1..high]
  putStrLn$ "Silver: "++ (show $maximum $ Map.elems scores)
  let (_, second, _) = foldl applyMarble (k, scores, ys) [high+1..high*100]
  putStrLn$ "Gold: "++ (show $maximum $ Map.elems second)

applyMarble :: GameState -> Int -> GameState
applyMarble (k, scores, ys) x = if mod x 23 /= 0 then (k, scores, typical x ys) else
  (k, Map.insertWith (+) (mod x k) (x + pop) scores, new) where (Just (pop, new)) = atypical ys

typical :: Int -> Circular -> Circular
typical x ys = cons x (iterate shiftLeft ys !! 2)

atypical :: Circular -> Maybe (Int, Circular)
atypical ys = uncons (iterate shiftRight ys !! 7)
