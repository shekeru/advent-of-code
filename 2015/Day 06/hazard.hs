{-# LANGUAGE TypeSynonymInstances #-}
module Main where

import Text.Printf
import Data.List.Lens
import Control.Lens
import Control.Monad.State
import Text.Parsec hiding (State)
import Text.Parsec.String

type Light = Bool
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
  toggle = not
  off _ = False
  on _ = True

main :: IO ()
main = do
  ln <- parseFromFile (many events) "input.txt"
  --printf "Silver: %d\n" $ length (filter isNice ln)
  print ln

eval :: [Event] -> State Grid
eval [] = get
eval (Event f start end:xs) = do
  mx <- get
  mx & ix (fst start)
events :: Parser Event
events = do
  statement <- choice (try.string <$> ["toggle", "turn off", "turn on"])
  let action = case last $ words statement of
        "toggle" -> toggle; "off" -> off; "on" -> on
  let number = read <$> many1 digit
  space; a <- number
  char ','; b <- number
  space *> manyTill anyChar space
  c <- number; char ',';
  d <- number; endOfLine
  pure $ Event action (a, c) (b, d)

grid :: Grid
grid = mk (mk False) where
  mk = replicate 1000
