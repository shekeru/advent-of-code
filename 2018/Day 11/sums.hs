module Main where

import qualified Data.Map.Strict as Map
import Control.Monad (replicateM)
import Data.List (maximumBy)
import Data.Function (on)

type Points = Map.Map (Int, Int) Int

main :: IO ()
main = do
  let xvs = yield 8141
  let (keys, value) = findMax xvs [3]
  let (keys', value') = findMax xvs [1..300]
  putStrLn$ "Silver: " ++ show keys ++ " with " ++ show value
  putStrLn$ "Gold: " ++ show keys' ++ " with " ++ show value'

findMax :: Points -> [Int] -> ([Int], Int)
findMax xvs = maximumBy (on compare snd) .concatMap (\j ->
  map (\[x,y] -> ([x+1,y+1,j], areaSum xvs j [x,y])) $coords j)
    where coords j = replicateM 2 [0..300 - j]

areaSum :: Points -> Int -> [Int] -> Int
areaSum xvs i [x,y] = sum [(if u == v then id else negate) $
  Map.findWithDefault 0 (x+u,y+v) xvs | v <- [0, i], u <- [0, i]]

yield :: Int -> Points
yield serial = foldl (apply serial)
  Map.empty $replicateM 2 [1..300]

apply :: Int -> Points -> [Int] -> Points
apply grid xvs [x,y] = Map.insert (x,y) value xvs where
  value = point + get (x-1, y) + get (x, y-1) - get (x-1, y-1)
  point = digit $ (10 + x) * (grid + (x + 10) * y)
  get k = Map.findWithDefault 0 k xvs
  digit n = mod (div n 100) 10 - 5
