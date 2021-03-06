{-# LANGUAGE PartialTypeSignatures, LambdaCase #-}
module Main where

import Text.Printf
import Control.Monad
import qualified Data.Map.Strict as SM
import Text.Parsec hiding (State)
import Text.Parsec.String
import Data.List

type Entry = (String, Int)
type Pair = (String, [Entry])
type Tree = SM.Map String [Entry]

main :: IO ()
main = do
  graph <- getFile; printf "Silver: %d\nGold: %d\n"
    (length (filter (silver graph) $SM.keys graph) - 1)
    (gold graph "shiny gold")

silver :: Tree -> String -> Bool
silver xs "shiny gold" = True
silver xs wh = any (silver xs.fst) $xs SM.! wh

gold :: Tree -> String -> Int
gold xs wh = sum $do
  (k, i) <- xs SM.! wh
  [i, i * gold xs k]

getFile :: IO Tree
getFile = parseFromFile (many stmnt) "input.txt" >>= \case
  Left err -> print err >> pure SM.empty
  Right inst -> pure $SM.fromList inst

stmnt :: Parser Pair
stmnt = do
    key <- chew $string " bag"
    value <- many $digit !!! inner
    chew endOfLine >> pure (key, value)

inner :: Parser Entry
inner = do
  i <- read <$> many1 digit
  w <- chew $string " bag"
  pure (tail w, i)

(!!!) :: Parser end -> Parser w -> Parser w
(!!!) cmp p = try $chew (lookAhead cmp) *> p

chew :: Parser end -> Parser String
chew = manyTill (noneOf "\n").try
