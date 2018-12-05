{-#LANGUAGE PartialTypeSignatures#-}
module Solution where

import qualified Data.IntMap.Lazy as Map
import Text.Parsec hiding (State)
import Text.Parsec.String
import Control.Monad.State
import Data.List.Split
import Control.Monad
import Text.Printf
import Data.List

data Entry = Entry {stamp :: String, time :: Int, event :: Action Int} deriving Show
data Action x = Wakes | Sleeps | Guard x deriving Show
type Matrix = Map.IntMap (Map.IntMap Int)
type Active = (Map.Key, Int, Matrix)

main :: IO()
main = do
  list <- sortOn stamp<$>input
  let result = (`evalState` start) $ trackTimes list
  print result where start = (0, 0, Map.empty)

input :: IO [Entry]
input = readFile "input.txt" >>= \y->
  pure$ case parse (many parseEvent) "" y of
    Left err -> []; Right xs -> xs

trackTimes :: [Entry] -> State Active Matrix
trackTimes [] = get >>= yield
  where yield (_, _, r) = pure r
trackTimes (action:future) = do
  (key, start, current) <- get
  let active = Map.findWithDefault Map.empty key current
  let new_state = update active [start..time action-1]
  case event action of
    Guard new -> put (new, start, current)
    Sleeps -> put (key, time action, current)
    Wakes -> put (key, start, Map.insert key
      new_state current)
  trackTimes future where
    update = foldl (\dict x -> Map.insertWith (+) x 1 dict)

parseEvent :: Parser Entry
parseEvent = do
  initial <- char '[' *> manyTill anyChar (char ']')
  let seconds = (read.last) $ splitOn ":" initial
  action <- spaces *> many letter
  value <- try (string " #" *> many1 digit)
    <|> manyTill anyChar newline
  try (manyTill anyChar newline)
  return$ Entry initial seconds $ case action of
    "falls" -> Sleeps; "wakes" -> Wakes
    "Guard" -> Guard $read value
