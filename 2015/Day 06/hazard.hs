{-# LANGUAGE PartialTypeSignatures, LambdaCase #-}
module Main where

import Control.Lens
import Control.Monad.State
import Text.Parsec hiding (State)
import Text.Parsec.String
import Text.Printf

type Coords = (Int, Int)
data Event = Event (Light -> Light) Coords Coords
data Light = Silver Bool | Gold Int
  deriving (Show, Eq, Ord)

class Matrix a where
  value :: a -> Int
  toggle :: a -> a
  off :: a -> a
  on :: a -> a

instance Matrix Light where
  -- Turn Off
  off (Gold x) = Gold $ max 0 (x - 1)
  off _ = Silver False
  -- Turn On
  on (Gold x) = Gold (x + 1)
  on _ = Silver True
  -- Toggle
  toggle (Silver x) = Silver $ not x
  toggle (Gold x) = Gold (x + 2)
  -- Value
  value (Silver x) = fromEnum x
  value (Gold x) = x

main :: IO ()
main = parseFromFile (many events)
  "input.txt" >>= \case
  Left err -> print err
  Right inst -> do
    printf "Silver: %d\n" $ evalState
      (loop inst) (grid $ Silver False)
    printf "Gold: %d\n" $ evalState
      (loop inst) (grid $ Gold 0)

loop :: [Event] -> State [[Light]] Int
loop [] = gets $ sum.map value.concat
loop (Event f xb yb:xs) = do
  get >>= put.(elements (bounded xb) . elements (bounded yb) %~ f)
  loop xs where bounded vs x = x >= fst vs && x <= snd vs

events :: Parser Event
events = do
  statement <- choice (try.string <$> ["toggle", "turn off", "turn on"])
  let action = case last $ words statement of
        "toggle" -> toggle; "off" -> off; _ -> on
  let number = read <$> many1 digit
  a <- space *> number
  b <- char ',' *> number <* space
  c <- manyTill anyChar space *> number
  d <- char ',' *> number <* endOfLine
  pure $ Event action (a, c) (b, d)

grid :: Light -> [[Light]]
grid f = mk (mk f) where
  mk = replicate 1000
