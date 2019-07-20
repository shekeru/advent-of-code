module Main where

import qualified Data.List.PointedList.Circular as List
import qualified Data.IntMap.Strict as Map
import Control.Monad (liftM2)

type GameState = (Int, Map.IntMap Int, Circular)
type Circular = List.PointedList Int

main :: IO()
main = solve 428 72061

solve :: Int -> Int -> IO()
solve players high = do
  let (k, scores, ys) = foldl applyMarble (players, Map.empty, List.singleton 0) [1..high]
  putStrLn$ "Silver: "++ (show $maximum $ Map.elems scores)
  let (_, second, _) = foldl applyMarble (k, scores, ys) [high+1..high*100]
  putStrLn$ "Gold: "++ (show $maximum $ Map.elems second)

applyMarble :: GameState -> Int -> GameState
applyMarble (k, scores, ys) x = if mod x 23 /= 0 then (k, scores, typical x ys) else
  (k, Map.insertWith (+) (mod x k) (x + pop) scores, new) where (pop, Just new) = atypical ys

typical :: Int -> Circular -> Circular
typical x ys = List.insert x (List.next ys)

atypical :: Circular -> (Int, Maybe Circular)
atypical ys = liftM2 (,) List._focus List.delete (List.moveN (-7) ys)
