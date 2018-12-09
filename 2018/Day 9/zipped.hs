module Main where

import qualified Data.IntMap.Lazy as Map

type GameState = (Int, Map.IntMap Int, Circular)
data Circular = Circular [Int] Int [Int]

main :: IO()
main = solve 428 72061

solve :: Int -> Int -> IO()
solve players high = do
  let (k, scores, ys) = foldl applyMarble (players, Map.empty, Circular [] 0 []) [1..high]
  putStrLn$ "Silver: "++ (show $maximum $ Map.elems scores)
  let (_, second, _) = foldl applyMarble (k, scores, ys) [high+1..high*100]
  putStrLn$ "Gold: "++ (show $maximum $ Map.elems second)

applyMarble :: GameState -> Int -> GameState
applyMarble (k, scores, ys) x = if mod x 23 /= 0 then (k, scores, typical x ys) else
  (k, Map.insertWith (+) (mod x k) (x + pop) scores, new) where (pop, new) = atypical ys

typical :: Int -> Circular -> Circular
typical x ys = commit x (move ys right 2)

atypical :: Circular -> (Int, Circular)
atypical ys = eject (move ys left 7)

right :: Circular -> Circular
right (Circular ls v (r:rs)) = Circular (v:ls) r rs
right (Circular ls v []) = Circular [] (head vs) ls'
  where (vs, ls') = splitAt 1 $reverse (v:ls)

left :: Circular -> Circular
left (Circular (l:ls) v rs) = Circular ls l (v:rs)
left (Circular [] v rs) = Circular rs' (head vs) []
  where (vs, rs') = splitAt 1 $reverse (v:rs)

commit :: Int -> Circular -> Circular
commit x (Circular ls v rs) = Circular ls x (v:rs)

move :: Circular -> (Circular -> Circular) -> Int -> Circular
move ys direction i = iterate direction ys !! i

eject :: Circular -> (Int, Circular)
eject (Circular ls v (r:rs)) = (v, Circular ls r rs)
eject (Circular ls v []) = (v, Circular [] (head vs) ls')
  where (vs, ls') = splitAt 1 $reverse ls
