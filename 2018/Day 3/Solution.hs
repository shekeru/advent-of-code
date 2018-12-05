{-#LANGUAGE PartialTypeSignatures, QuasiQuotes#-}
module Solution where

import qualified Data.IntMap.Lazy as Map
import Control.Monad.State
import Text.RE.TDFA.String
import Data.Function
import Text.Printf
import Data.List

data Claim = Claim {rec :: Int, zone :: Map.IntMap Int} deriving Show

main :: IO()
main = print ""

input :: IO [[Int]]
input = map regex.lines <$> readFile "input.txt"

regex :: Read b => String -> [b]
regex = map read.matches.(*=~ [re|@{%int}|])
