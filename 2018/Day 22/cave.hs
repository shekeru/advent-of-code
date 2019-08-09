module Main where

import Text.Printf
import qualified Data.HashMap.Strict as SM
import System.IO.Unsafe
import Data.IORef

type Location = (Int, Int)
data Position = Position Location
  Equipment deriving (Show, Eq)
data Equipment = Torch | Gear
  | Free deriving (Show, Eq)

main :: IO ()
main = do
  printf "Silver: %d\n" silver
  printf "Gold: %d\n" silver

target :: Location
target = (8, 713)
depth = 3879

silver :: Int
silver = sum $ do
  x <- [0..a]; y <- [0..b]
  pure $ level (x, y) where
    (a, b) = target

level :: Location -> Int
level z = mod (erode z) 3

erode :: Location -> Int
erode z = unsafePerformIO $ do
  cache <- readIORef world
  case SM.lookup z cache of
    Just value -> return value
    Nothing -> do
      modifyIORef' world $ SM.insert z
        (mod (index z + depth) 20183)
      pure $ erode z

index :: Location -> Int
index z@(x, y)
  | z == (0, 0) = 0
  | z == target = 0
  | z == (0, y) = y * 48271
  | z == (x, 0) = x * 16807
  | otherwise = erode (x - 1, y)
    * erode (x, y - 1)

world :: IORef (SM.HashMap Location Int)
world = unsafePerformIO (newIORef SM.empty)
{-# NOINLINE world #-}
