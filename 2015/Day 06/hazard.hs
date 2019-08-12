{-# LANGUAGE TypeSynonymInstances #-}
module Main where

import Data.List
import Text.Printf
import Data.List.Lens
import Control.Lens

type Light = Bool
type Grid = [[Light]]

class Toggle a where
  toggle :: a -> a
  off :: a -> a
  on :: a -> a

instance Toggle Light where
  toggle = not
  off _ = False
  on _ = True

main :: IO ()
main = do
  ln <- lines <$> readFile "input.txt"
  --printf "Silver: %d\n" $ length (filter isNice ln)
  print ""

grid :: Grid
grid = mk (mk False) where
  mk = replicate 1000
