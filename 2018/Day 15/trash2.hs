{-# LANGUAGE PartialTypeSignatures, TemplateHaskell, FlexibleInstances #-}
module Main where

import Data.List
import Data.Function
import Control.Monad
import qualified Data.Map.Lazy as LM
import Control.Lens.At
import Control.Lens

import Debug.Trace
import Text.Printf

type Coords = (Int, Int)
type World = LM.Map Coords Entity
data Faction = Goblin | Elves deriving (Show, Eq)
data Entity = Slot | Wall | Unit {
  _side :: Faction, _hp :: Int, _dmg :: Int
} deriving (Eq)
makeLenses ''Entity

instance {-# OVERLAPPING #-} Show World where
  show = concatMap show
instance {-# OVERLAPPING #-} Show [Entity] where
  show xs = concatMap show xs ++ "\n"
instance Show Entity where
  show (Unit t _ _) = case t of
    Goblin -> "G"
    Elves -> "E"
  show Wall = "#"
  show _ = "."

main :: IO ()
main = do
  silver <- simulate <$> input
  print silver
  -- printf "Silver: %d\n" silver

input :: IO World
input = do
  xss <- lines <$> readFile "test0.txt"
  return $ map (map addTile) xss

addTile :: Char -> Entity
addTile 'G' = Unit Goblin 200 3
addTile 'E' = Unit Elves 200 3
addTile '#' = Wall
addTile _ = Slot

simulate world = do
  let mstep
  let (a, tc) = mapAccumL step world
