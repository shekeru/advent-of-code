{-#LANGUAGE PartialTypeSignatures, QuasiQuotes#-}
module Solution where

import qualified Data.Map.Lazy as Map
import qualified Data.Set as Set
import Control.Monad.State
import Text.RE.TDFA.String
import Data.Function
import Text.Printf
import Data.List

type Fabric = Map.Map Int Claim
type Claim = Map.Map Coords Int
type Coords = (Int, Int)

main :: IO()
main = do
  matrix <- Map.fromList.map expand<$>input
  let overlapped = overlap matrix :: Claim
  printf "part 1: %d\n" $ reduce overlapped
  printf "part 2: %d\n" $ isolate overlapped matrix

input :: IO [[Int]]
input = map regex.lines <$> readFile "input.txt"

regex :: Read b => String -> [b]
regex = map read.matches.(*=~ [re|@{%int}|])

expand :: [Int] -> (Int, Claim)
expand [i, x, y, w, h] = (i, Map.fromSet (const 1) lazy_map) where
  lazy_map = Set.fromAscList.map (\[a,b] ->
    (a, b)).sequence $ [[y..y+h-1], [x..x+w-1]]

overlap :: Fabric -> Claim
overlap = Map.unionsWith (+). Map.elems

reduce :: Claim -> Int
reduce = foldr qualify 0 where
  qualify x y = if x>1 then y+1 else y

isolate :: Claim -> Fabric -> Int
isolate master = head. Map.keys. Map.filter match where
  match dict = (== ) dict $Map.intersection master dict
