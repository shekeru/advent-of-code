{-# LANGUAGE PartialTypeSignatures, LambdaCase #-}

import Control.Arrow
import Data.Function (on)
import Text.Parsec hiding (State)
import Data.Map (Map, fromList, empty)
import Text.Parsec.String
import Text.Printf

type Pair = (Int, String)
type Entry = (Int, [Pair])
type Graph = Map String Entry
type Reaction = (String, Entry)

main :: IO()
main = do
  xs <- getFile
  print xs

getFile :: IO Graph
getFile = parseFromFile (many1
    reaction) "ins.txt" >>= \case
  Left err -> print err >> pure empty
  Right inst -> pure $ fromList inst

reaction :: Parser Reaction
reaction = do
  body <- pair `sepBy` string ", "
  (x, name) <- string " => " *> pair
  endOfLine >> pure (name, (x, body))

pair :: Parser Pair
pair = do
  coeff <- read <$> many1 digit
  name <- space *> many1 letter
  return (coeff, name)
