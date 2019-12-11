{-# LANGUAGE TemplateHaskell, PartialTypeSignatures, LambdaCase #-}
module Main where

import Text.Printf
import Control.Monad
import Control.Arrow
import Data.List.Split
import qualified Data.Map.Strict as SM
import Control.Applicative
import Control.Lens.TH
import Control.Lens
import IntCode

type Direction = Int
type Coords = (Int, Int)
type Space = SM.Map Coords Int
data Turtle = Turtle {
  _dir :: Direction,
  _coords :: Coords,
  _tiles :: Space
} deriving Show
$(makeLenses ''Turtle)

main :: IO()
main = do
  turtle <- draw.eval <$> input
  let [test, real] = map turtle [[], [1]]
  printf "Silver: %d\n" (length test)
  let (y0, x0) = fst(SM.findMin real)
  let (y1, x1) = fst(SM.findMax real)
  forM_ [y0..y1]$ \y -> do
    forM_ [x0..x1]$ \x -> putChar$ if 0
      < nil (y, x) real then '#' else ' '
    putChar '\n'

draw :: (Input -> Output) -> Input -> Space
draw code xs = last st ^. tiles where
  st = chunksOf 2 ys& scanl move new
  new = Turtle 0 (0, 0) SM.empty
  ys = xs++ map camera st& code
nil = SM.findWithDefault 0

move :: Turtle -> [Int] -> Turtle
move st [x, y] = st' where
  st' = st & dir %~ turn y
    & tiles %~ paint st x
    & coords %~ fwds st'

camera :: Turtle -> Int
camera = liftA2 nil _coords _tiles

paint :: Turtle -> Int -> (Space -> Space)
paint st = SM.insert (_coords st)

fwds :: Turtle -> (Coords -> Coords)
fwds = _dir >>> \case
  1 -> second (+1)
  3 -> second (subtract 1)
  0 -> first (subtract 1)
  2 -> first (+1)

turn :: Int -> Int -> Int
turn tn ptr = flip mod 4$ ptr
  + if tn > 0 then 1 else -1
