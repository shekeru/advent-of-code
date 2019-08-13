{-# LANGUAGE PartialTypeSignatures, QuasiQuotes #-}
module Main where

import Text.RE.Tools
import Text.RE.TDFA.String
import Text.Printf
import Data.Char

main :: IO ()
main = let prompt ys x = printf x (sum ys) in do
  ln <- lines <$>
    readFile "input.txt"
  prompt (silver ln) "Silver: %d\n"
  prompt (gold ln) "Gold: %d\n"

silver :: [String] -> [Int]
silver xs = zipWith id ((-).length <$> xs) $
  map length (read.adjust <$> xs :: [String])

gold :: [String] -> [Int]
gold xs = zipWith id ((-).length.show <$> xs) $ map length xs

adjust :: String -> String
adjust xs = replaceAllCaptures ALL fuck (xs *=~ [re|\\x[0-9a-f]{2}|])
 where fuck _ _ cpt = Just $ fst <$> readLitChar (capturedText cpt)
