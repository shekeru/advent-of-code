{-# LANGUAGE PartialTypeSignatures, TemplateHaskell  #-}
module Main where

import Text.Printf
import qualified Data.Map.Strict as SM
import System.IO.Unsafe
import Control.Lens.TH
-- import Control.Monad
-- import Control.Lens
import Data.IORef
import Data.List

type Location = (Int, Int)
type SearchQueue = [Position]
data Equipment = Nil | Torch | Gear
  deriving (Show, Eq, Enum, Bounded)
data Position = Position {
  _coords :: Location,
  _slot :: Equipment,
  _cost :: Int
} deriving (Show, Eq)
$(makeLenses ''Position)
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
  -- forM_ [Torch, Gear, Free] $ \c -> do
  --   forM_ [0..snd target] $ \y -> do
  --     forM_ [0..fst target] $ \x ->
  --        printf "%d " $ cost c $ level (x, y)
  --     putStr "\n"
  --   putStr "\n"
  --printf "Gold: %d\n" silver

silver :: Int
silver = sum $ do
  x <- [0..a]; y <- [0..b]
  pure $ level (x, y) where
    (a, b) = target

-- Second Level
g = iterate step start

k = head $ head $ dropWhile (\xs ->
  target /= (_coords $ head xs)) g

start :: SearchQueue
start = [Position (0, 0) Torch 0]

step :: SearchQueue -> SearchQueue
step (x:xs) = unsafePerformIO $ do
  let ys = filter past $ foldl insertOrd xs $ nb4 x
  modifyIORef' seen $ SM.insertWith
    min (_coords x) (_cost x); pure ys
step mempty = mempty

insertOrd :: SearchQueue -> Position -> SearchQueue
insertOrd (x:xs) y
  | _cost x > _cost y = y : x : xs
  | otherwise = x : insertOrd xs y
insertOrd [] y = [y]

nb4 :: Position -> [Position]
nb4 z@(Position (x, y) _ c) = concatMap (move z)
  [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]

move :: Position -> Location -> [Position]
move (Position orig eq cost) z@(x, y) | invalid z = mempty
  | eq /= toEnum (level z) = [Position z eq (cost+1)]
  | otherwise = (<$> [pred' eq, succ' eq]) $
    \new -> Position z new $ cost + 8

invalid :: Location -> Bool
invalid (x,y) = x < 0 || y < 0 || x >
  fst target + 4 || y > snd target + 4

peek = unsafePerformIO $ do
  cache <- readIORef seen
  return (cache SM.! target)

past :: Position -> Bool
past x@(Position z _ c) = unsafePerformIO $ do
  cache <- readIORef seen
  pure $ case SM.lookup z cache of
        Just v -> v > c; Nothing -> True

seen :: IORef (SM.Map Location Int)
seen = unsafePerformIO (newIORef SM.empty)
{-# NOINLINE seen #-}

-- ref :: Position -> Position
-- ref pos = unsafePerformIO $ modifyIORef' routes
--   (SM.insertWith f (_coords pos) pos) >> pure pos where
--     f n o = if _cost o <= _cost n then o else n

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
