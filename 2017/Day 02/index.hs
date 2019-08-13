{-# LANGUAGE PartialTypeSignatures, LambdaCase #-}
module Main where

import Text.Printf
import Text.Parsec hiding (State)
import Text.Parsec.String

type Row = [Int]

main :: IO ()
main = do
  xss <- eval
  let prompt s f = printf s $ sum (f <$> xss)
  prompt "Silver: %d\n" part1
  prompt "Gold: %d\n" part2

part2 :: Row -> Int
part2 xs = maximum $ ck <$> xs <*> xs where
  ck a b = if mod a b > 0 then 0 else div a b

part1 :: Row -> Int
part1 xs = maximum xs
  - minimum xs

eval :: IO [Row]
eval = parseFromFile (many rows)
  "input.txt" >>= \case
  Right values -> pure values
  Left err -> print err >> pure []

rows :: Parser Row
rows = do
  let int = many1 digit
  let num = try (int <* char '\t') <|> int
  map read <$> manyTill num endOfLine
