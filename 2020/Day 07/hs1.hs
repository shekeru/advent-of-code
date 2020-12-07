{-# LANGUAGE PartialTypeSignatures, LambdaCase #-}

import Text.Printf
import Control.Monad
import qualified Data.Map.Strict as SM
import Text.Parsec hiding (State)
import Text.Parsec.String
import Data.List 

type Entry = (String, Int)
type Pair = (String, [Entry])
type Graph = SM.Map String [Entry]

main :: IO ()
main = do
  graph <- getFile; let fn x = x graph "shiny gold"
  printf "Silver: %d\nGold: %d\n" (length $fn silver) (fn gold)

silver :: Graph -> String -> [String]
silver xs wh = nub$ SM.foldlWithKey fuck [] xs where
  fuck ys k v = foldl (flip (:)) ys $do
    guard (elem wh $map fst v)
    k : silver xs k

gold :: Graph -> String -> Int
gold xs wh = sum $do
  (k, i) <- xs SM.! wh
  [i, i * gold xs k]

getFile :: IO Graph
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
