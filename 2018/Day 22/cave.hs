{-# LANGUAGE PartialTypeSignatures, TemplateHaskell  #-}
module Main where

import Text.Printf
import qualified Data.PQueue.Min as PQ
import qualified Data.Map.Strict as SM
import System.IO.Unsafe
import Data.Either
import Data.IORef

type Location = (Int, Int)
type SearchQueue = (SM.Map (Location, Equipment) Int, PQ.MinQueue Position)
data Equipment = Nil | Torch | Gear
  deriving (Show, Eq, Enum, Bounded, Ord)
data Position = Position {
  _coords :: Location,
  _slot :: Equipment,
  _cost :: Int
} deriving (Show, Eq)
type Terrain = Int

instance Ord Position where
  x <= y = _cost x <= _cost y

pred' x = if x == minBound then
  maxBound else pred x
succ' x = if x == maxBound then
  minBound else succ x

depth :: Int
depth = 3879
target :: Location
target = (8, 713)

-- Main Program
main :: IO ()
main = do
  printf "Silver: %d\n" silver
  let ys = filter isRight $ iterate step (Left start)
  print $ head ys

silver :: Int
silver = sum $ do
  x <- [0..a]; y <- [0..b]
  pure $ level (x, y) where
    (a, b) = target

-- Second Level
start :: SearchQueue
start = (SM.empty, PQ.singleton (Position (0, 0) Torch 0))

step :: Either SearchQueue Int -> Either SearchQueue Int
step (Left (seen, hxq))
  | PQ.null hxq = Left (seen, hxq)
  | SM.member (target, Torch) seen = Right $ seen SM.! (target, Torch)
  | otherwise = do
  let (x, xs) = PQ.deleteFindMin hxq
  let toContinue = case SM.lookup (_coords x, _slot x) seen of
        Nothing -> True; Just v -> v > _cost x
  Left $ if toContinue then (SM.insert (_coords x, _slot x) (_cost x)
    seen, PQ.union xs $ PQ.fromList $ nb4 x) else (seen, xs)
step (Right int) = Right int

nb4 :: Position -> [Position]
nb4 z@(Position (x, y) _ c) = concatMap (move z)
  [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

move :: Position -> Location -> [Position]
move (Position orig eq cost) z@(x, y) | invalid z = mempty
  | eq /= toEnum (level z) = [Position z eq (cost+1)]
  | otherwise = [Position orig (head $ filter (/= toEnum
    (level orig)) [pred' eq, succ' eq]) (cost + 7)]

invalid :: Location -> Bool
invalid (x,y) = x < 0 || y < 0 || x >
  fst target + 49 || y > snd target + 49

-- Shared Functions
level :: Location -> Terrain
level z = mod (erode z) 3

erode :: Location -> Int
erode z = unsafePerformIO $ do
  cache <- readIORef world
  case SM.lookup z cache of
    Just value -> return value
    Nothing -> do
      modifyIORef' world $ SM.insert z
        (mod (geoIx z + depth) 20183)
      pure $ erode z

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
