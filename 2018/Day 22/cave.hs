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
data Equipment = Nil | Torch | Gear
  deriving (Show, Eq, Enum, Bounded)
data Position = Position {
  _coords :: Location,
  _slot :: Equipment,
  _cost :: Int
} deriving (Show, Eq)
$(makeLenses ''Position)
type Terrain = Int
type Cost = Int

instance Ord Position where
  x <= y = _cost x <= _cost y

pred' x = if x == minBound then
  maxBound else pred x
succ' x = if x == maxBound then
  minBound else succ x

g = iterate search start

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

depth :: Int
depth = 3879
target :: Location
target = (8, 713)
-- target = (10, 10)
-- depth = 510

silver :: Int
silver = sum $ do
  x <- [0..a]; y <- [0..b]
  pure $ level (x, y) where
    (a, b) = target

start = [Position (0, 0) Torch 0]

search :: [Position] -> [Position]
search [] = mempty
search (x:xs) = unsafePerformIO $ do
  cache <- readIORef routes
  pure $ if limit cache x then
    xs ++ nb x else xs

limit :: SM.Map Location Position -> Position -> Bool
limit cache pos = case SM.lookup (_coords pos) cache of
  Nothing -> True; Just old -> _cost old + 16 > _cost pos

nb4 :: Position -> [Position]
nb4 z@(Position (x, y) _ _) = concatMap (move $ ref z)
  [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]

move :: Position -> Location -> [Position]
move (Position orig eq cost) z@(x, y) | invalid z = mempty
  | eq /= toEnum (level z) = [Position z eq (cost+1)]
  | otherwise = (<$> [pred' eq, succ' eq]) $
    \new -> Position z new $ cost + 8

meh readIORef routes >>= pure.SM.lookup target

invalid :: Location -> Bool
invalid (x, y) = x < 0 || y < 0 || x >
  fst target + 10 || y > snd target + 10

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

ref :: Position -> Position
ref pos = unsafePerformIO $ modifyIORef' routes
  (SM.insertWith f (_coords pos) pos) >> pure pos where
    f n o = if _cost o <= _cost n then o else n

routes :: IORef (SM.Map Location Position)
routes = unsafePerformIO (newIORef SM.empty)
{-# NOINLINE routes #-}

world :: IORef (SM.Map Location Int)
world = unsafePerformIO (newIORef SM.empty)
{-# NOINLINE world #-}
