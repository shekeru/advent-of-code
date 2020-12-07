{-# LANGUAGE PartialTypeSignatures, LambdaCase, TupleSections #-}
module Main where

import Text.Printf (printf)
import Control.Monad (guard)
import qualified Data.Map.Strict as SM
import Text.Parsec hiding (State)
import Data.Function ((&))
import Text.Parsec.String
import Data.List (nub)

type Entry = (String, Int)
type Pair = (String, [Entry])
type Tree = SM.Map String [Entry]

main :: IO ()
main = do
  graph <- getFile; let fn x = x graph "shiny gold"
  printf "Silver: %d\n" $silver &length.nub.fn
  printf "Gold: %d\n" $fn gold

silver :: Tree -> String -> [String]
silver xs wh = (`SM.foldMapWithKey` xs)$ \k v ->
  guard (elem wh $map fst v) >> k : silver xs k

gold :: Tree -> String -> Int
gold xs wh = sum $do
  (k, i) <- xs SM.! wh
  [i, i * gold xs k]

getFile :: IO Tree
getFile = parseFromFile (many stmnt) "input.txt" >>= \case
  Left err -> print err >> pure SM.empty
  Right inst -> pure $SM.fromList inst

stmnt :: Parser Pair
stmnt = let color = chew $string " bag" in do
    key <- color; value <- (<* chew endOfLine) $many $read <$> (try.chew.
      lookAhead >>= (*>)) (many1 digit) >>= \i -> color >>= pure.(, i).tail
    pure (key, value) where chew = manyTill (noneOf "\n").try
