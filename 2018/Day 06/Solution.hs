{-#LANGUAGE PartialTypeSignatures#-}
module Main where

import qualified Data.Map.Lazy as Map
import Control.Monad.State
import Data.List.Split
import Data.Function
import Text.Printf
import Data.List

type Counter = Map.Map Coords Int
type Coords = (Int, Int)

unpair (a,b) = [a,b]
pair [a,b] = (a,b)

main :: IO()
main = do
  points <- input
  let start = (points, Map.empty, 0)
  let ranges = pair <$> (mapM range.unpair.unzip) points
  let result = distance ranges `evalState` start
  printf "part 1: %d\n" $fst result
  printf "part 2: %d\n" $snd result

input :: IO [Coords]
input = map (pair.parse).lines<$>readFile "input.txt"
  where parse = map read.splitOn ","

distance :: [Coords] -> State ([Coords], Counter, Int) (Int, Int)
distance [] = gets yield where
  yield (_, m, t) = (maximum $Map.elems m, t)
distance (p:next) = do
  (points, tracking, total) <- get
  put (points, case nearest points p of
    Just match -> Map.insertWith (+) match 1 tracking
    Nothing -> tracking, if closeby points p then
      total + 1 else total); distance next

nearest :: [Coords] -> Coords -> Maybe Coords
nearest points p = do
  let table = m_dist' p <$> points
  let (val, key) = minimumBy (on compare fst) table
  if count (map fst table) val == 1 then Just key else Nothing

closeby :: [Coords] -> Coords -> Bool
closeby points p = 10000 > (sum $m_dist p <$> points)

m_dist :: Coords -> Coords -> Int
m_dist (x1,y1) (x,y) = on (+) abs (x1-x) (y1-y)

m_dist' :: Coords -> Coords -> (Int, Coords)
m_dist' a b = (m_dist a b, b)

range :: (Foldable t, Ord a, Num a, Enum a) => t a -> [a]
range ys = [minimum ys..maximum ys-1]

count :: Eq a => [a] -> a -> Int
count xs x = length $filter (== x) xs
