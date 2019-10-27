{-# LANGUAGE PartialTypeSignatures #-}
module Main where

import Text.Printf
import Data.Foldable (foldl')
import qualified Data.PQueue.Min as PQ
import qualified Data.Map.Strict as SM
import qualified Data.Set as SS
import Debug.Trace
import System.IO.Unsafe
import Data.Either
import Data.IORef

type Location = (Int, Int)
type World = SM.Map Location Int
type Visited = SS.Set (Location, Equipment)
type Queue = PQ.MinQueue Position
type SearchQueue = (Visited, Queue)
data Equipment = Nil | Torch | Gear
  deriving (Show, Eq, Enum, Ord)
data Position = Position {
  _coords :: Location,
  _slot :: Equipment,
  _cost :: Int
} deriving (Show, Eq)
type Terrain = Int

instance Ord Position where
  x <= y = qval x <= qval y where
    qval (Position (x,y) eq c) = c + abs
      (fst target - x) + abs (snd target - y)

depth :: Int
depth = 3879
target :: Location
target = (8, 713)

-- Main Program
main :: IO ()
main = do
  printf "Silver: %d\n" silver
  printf "Gold: %d\n" (step start)

silver :: Int
silver = sum $ do
  x <- [0..a]; y <- [0..b]
  pure $ level (x, y) where
    (a, b) = target

-- Second Level
start :: SearchQueue
start = (SS.empty, PQ.singleton
  (Position (0, 0) Torch 0))

step :: SearchQueue -> Int
step (seen, hxq) = let (x, xs) = traceShow ("Visited: " ++ show (length seen)) $ PQ.deleteFindMin hxq in if
  (_coords x == target) && (_slot x == Torch) then _cost x else step $ if
    SS.notMember (_coords x, _slot x) seen then (SS.insert (_coords x, _slot x) seen,
      foldl' pqIns xs $ nb4 $ traceShowId x) else (seen, xs) where pqIns obj a = PQ.insert a obj

nb4 :: Position -> [Position]
nb4 z@(Position (x, y) _ c) = concatMap (move z)
  [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]

move :: Position -> Location -> [Position]
move (Position orig eq cost) z@(x, y) | invalid z = mempty
  | z == target = pure $ Position z Torch $
    cost + if eq == Torch then 1 else 8
  | eq /= toEnum (level z) = [Position z eq (cost + 1)]
  | otherwise = [Position z (toEnum $ morph
    (level z) $ level orig) (cost + 8)]

morph :: Int -> Int -> Int
morph 0 1 = 2; morph 1 0 = 2
morph 0 2 = 1; morph 2 0 = 1
morph 1 2 = 0; morph 2 1 = 0

invalid :: Location -> Bool
invalid (x,y) = x < 0 || y < 0 ||
  x > fst target + 52

-- Shared Functions
level :: Location -> Terrain
level z = mod (erode z) 3

erode :: Location -> Int
erode z = unsafePerformIO $ do
  cache <- readIORef world
  case SM.lookup z cache of
    Just value -> return value
    Nothing -> do
      putStrLn $ "Stuck in IO: " ++ show z
      let val = mod (geoIx z + depth) 20183
      modifyIORef' world $ SM.insert z val
      return val

geoIx :: Location -> Int
geoIx z@(x, y)
  | z == (0, 0) = 0
  | z == target = 0
  | z == (0, y) = y * 48271
  | z == (x, 0) = x * 16807
  | otherwise = erode (x - 1, y)
    * erode (x, y - 1)

world :: IORef (SM.Map Location Int)
world = unsafePerformIO (newIORef SM.empty)
{-# NOINLINE world #-}
