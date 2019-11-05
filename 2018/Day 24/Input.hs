{-# LANGUAGE PartialTypeSignatures, LambdaCase #-}
module Input where

import Text.Parsec hiding (State)
import Text.Parsec.String
import Data.Function

type Mods = (String, [String])
data Group = Group {
    _units :: Int,
    _hitPoints :: Int,
    _immunities :: [String],
    _weaknesses :: [String],
    _attackDamage :: Int,
    _attackType :: String,
    _initiative :: Int,
    _system :: String
} deriving (Show)

instance Eq Group where
  (==) = on (==) _initiative

getFile :: IO [Group]
getFile = parseFromFile (section `sepBy`
  endOfLine) "input.txt" >>= \case
  Left err -> print err >> pure []
  Right inst -> pure $ concat inst

section :: Parser [Group]
section = do
  system <- chew (char ':') <* endOfLine
  many1 (line system <* endOfLine)

publish :: [Mods] -> Group -> Parser Group
publish (("immune", x) : xs) group =
  publish xs $ group {_immunities = x}
publish (("weak", x) : xs) group =
  publish xs $ group {_weaknesses = x}
publish [] group = return group

line :: String -> Parser Group
line system = do
    units <- number
    hp <- (digit !!! number)
      <* string " hit points "
    mods <- option [] typeInfo
    dmg <- digit !!! number
    aspect <- space *> many1 letter
    order <- digit !!! number
    publish mods $ Group units hp []
      [] dmg aspect order system

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
