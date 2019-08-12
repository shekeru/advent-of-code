{-# LANGUAGE TypeSynonymInstances, PartialTypeSignatures #-}
module Main where

import Text.Printf
import Data.List.Lens
import Control.Lens
import Control.Monad.State
import Text.Parsec hiding (State)
import Text.Parsec.String

data Light = Off | On
  deriving (Show, Eq, Enum)
type Grid = [[Light]]
type Coords = (Int, Int)
data Event = Event (Light -> Light) Coords Coords

instance Show Event where
  show (Event f a b) = show a ++ show b

class Toggle a where
  toggle :: a -> a
  off :: a -> a
  on :: a -> a

instance Toggle Light where
  toggle On = Off
  toggle Off = On
  off = const Off
  on = const On

main :: IO ()
main = do
  ln <- parseFromFile (many events) "input.txt"
  case ln of
    Left err -> print err
    Right value -> do
      print $ evalState (loop value) grid
  --printf "Silver: %d\n" $ length (filter isNice ln)

loop :: [Event] -> State Grid Int
loop [] = gets $ sum.map (sum.map fromEnum)
loop (Event f xb yb:xs) = do
  current <- get
  put $ current & elements (`elem` [fst xb..snd xb]) .
        elements (`elem` [fst yb..snd yb]) %~ f
  loop xs

events :: Parser Event
events = do
  statement <- choice (try.string <$> ["toggle", "turn off", "turn on"])
  let action = case last $ words statement of
        "toggle" -> toggle; "off" -> off; "on" -> on
  let number = read <$> many1 digit
  a <- space *> number
  b <- char ',' *> number
  space *> manyTill anyChar space
  c <- number; d <- char ',' *> number
  endOfLine; pure $ Event action (a, c) (b, d)

grid :: Grid
grid = mk (mk Off) where
  mk = replicate 1000
