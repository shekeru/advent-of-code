{-# LANGUAGE PartialTypeSignatures, LambdaCase #-}
module Input where

import Text.Parsec hiding (State)
import Text.Parsec.String

data Group = Group {
    _units :: Int,
    _hp :: Int,
    _immune :: [String],
    _weak :: [String],
    _dmg :: Int,
    _aspect :: String,
    _order:: Int
} deriving (Show)

getFile :: IO _
getFile = parseFromFile (line)
  "input.txt" >>= \case
  Left err -> print err >> pure []
  Right inst -> pure [inst]

line :: Parser Group
line = do
    units <- number
    hp <- burn *> 
        number
    dmg <- burn *> 
        number
    aspect <- space *>
        many1 letter
    order <- burn *> 
        number
    pure $ Group units hp [] [] 
        dmg aspect order

burn :: Parser String
burn = chew digit

number :: Parser Int
number = read <$> many1 digit

chew :: _ -> _
chew = manyTill anyChar.lookAhead 
