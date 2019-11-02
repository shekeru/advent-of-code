{-# LANGUAGE PartialTypeSignatures, LambdaCase #-}
module Input where

import Text.Parsec hiding (State)
import Text.Parsec.String

type Mods = (String, [String])
type Section = (String, [Group])
data Group = Group {
    _units :: Int,
    _hitPoints :: Int,
    _immunities :: [String],
    _weaknesses :: [String],
    _attackDamage :: Int,
    _attackType :: String,
    _initiative :: Int
} deriving (Show)

getFile :: IO [Section]
getFile = parseFromFile (section `sepBy` endOfLine)
  "input.txt" >>= \case
  Left err -> print err >> pure []
  Right inst -> pure inst

section :: Parser Section
section = do
  system <- chew (char ':') <* endOfLine
  groups <- many1 (line <* endOfLine)
  return (system, groups)

publish :: [Mods] -> Group -> Parser Group
publish (("immune", x) : xs) group =
  publish xs $ group {_immunities = x}
publish (("weak", x) : xs) group =
  publish xs $ group {_weaknesses = x}
publish [] group = return group

line :: Parser Group
line = do
    units <- number
    hp <- (digit !!! number)
      <* string " hit points "
    mods <- option [] typeInfo
    dmg <- digit !!! number
    aspect <- space *> many1 letter
    order <- digit !!! number
    publish mods $ Group units hp []
      [] dmg aspect order

typeInfo :: Parser [Mods]
typeInfo = between (char '(') (char ')')
  (types `sepBy` string "; ")

types :: Parser Mods
types = do
  modify <- many1 letter <* string " to "
  what <- many1 letter `sepBy` string ", "
  pure (modify, what)

number :: Parser Int
number = read <$> many1 digit

(!!!) :: Parser end -> Parser w -> Parser w
(!!!) cmp p = chew (lookAhead cmp) *> p

chew :: Parser end -> Parser String
chew = manyTill anyChar
