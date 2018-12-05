{-#LANGUAGE PartialTypeSignatures#-}
module Solution where

import qualified Data.IntMap.Lazy as Map
import Text.Parsec hiding (State)
import Text.Parsec.String
import Control.Monad.State
import Data.List.Split
import Data.Function
import Text.Printf
import Data.List

data Entry = Entry {stamp :: String, time :: Int, event :: Action Int} deriving Show
data Action x = Wakes | Sleeps | Guard x deriving Show
type Matrix = Map.IntMap (Map.IntMap Int)
type Active = (Map.Key, Int, Matrix)

main :: IO()
main = (sortOn stamp<$>input) >>= \y ->
  mapM_ ($trackTimes y `evalState` start) [
    printf "part 1: %d\n".solve sum,
    printf "part 2: %d\n".solve maximum
    ] where start = (0, 0, Map.empty)

input :: IO [Entry]
input = readFile "input.txt" >>= \y ->
  pure$ case parse (many parseEvent) "" y of
    Left err -> []; Right xs -> xs

solve :: (Map.IntMap Int -> Int) -> Matrix -> Int
solve func kxvs = key * value where
  greatest = maximumBy (compare `on` snd).Map.assocs
  (key, _) =  greatest $Map.map func kxvs
  (value, _) = greatest (kxvs Map.! key)

trackTimes :: [Entry] -> State Active Matrix
trackTimes [] = get >>= yield
  where yield (_, _, r) = pure r
trackTimes (action:remaining) = do
  (key, start, current) <- get
  let active = Map.findWithDefault Map.empty key current
  let new_state = update active [start..time action-1]
  put $ case event action of
    Wakes -> (key, start, Map.insert key new_state current)
    Sleeps -> (key, time action, current)
    Guard new -> (new, start, current)
  trackTimes remaining where
    update = foldl (\dict x -> Map.insertWith (+) x 1 dict)

parseEvent :: Parser Entry
parseEvent = do
  initial <- char '[' *> manyTill anyChar (char ']')
  let seconds = (read.last) $ splitOn ":" initial
  action <- spaces *> many letter
  value <- try (string " #" *> many1 digit)
    <|> many space; manyTill anyChar endOfLine
  return$ Entry initial seconds $ case action of
    "falls" -> Sleeps; "wakes" -> Wakes
    "Guard" -> Guard $read value
