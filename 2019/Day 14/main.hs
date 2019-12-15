{-# LANGUAGE PartialTypeSignatures, LambdaCase, ScopedTypeVariables #-}

import Text.Parsec
import Text.Parsec.String
import Control.Lens.At
import Control.Lens
import Control.Arrow
import Data.Map.Strict hiding
  (head, foldl, filter)
import Data.Function
import Text.Printf

type Component = (Int, Element)
type Table = (Int, [Component])
type Reactions = Map Element Table
type Amounts = Map Element Int
type Element = String

main :: IO()
main = do
  react <- solve <$> getFile
  react 1 & printf "Silver: %d\n"
  let limit = 1e24 / fromIntegral
        (10^12 & react) & truncate
  [limit, limit-1..] & printf
    "Gold: %d\n".head.dropWhile
    (\x -> react x > 10^12)

solve :: Reactions -> Int -> Int
solve xs =
  singleton "FUEL" >>>
  iterate (reduce $calc xs) >>>
  dropWhile (not.balanced) >>>
  head >>> (! "ORE")

balanced :: Amounts -> Bool
balanced = foldlWithKey fn True where
  fn a k v = a && (k == "ORE" || v <= 0)

reduce :: (Amounts -> Element -> Amounts) -> Amounts -> Amounts
reduce calc tree = foldl calc tree $filter
  (\x -> x /= "ORE" && tree !x > 0) $keys tree

calc :: Reactions -> Amounts -> Element -> Amounts
calc graph tree pt = cock $foldl create tree table where
  create :: Amounts -> Component -> Amounts
  create tree (a, x) = tree &at x.non 0 +~ a * y'
  y' = ceiling $on (/) fromIntegral (tree !pt) y
  cock var = var &at pt.non 0 -~ y * y'
  cock :: Amounts -> Amounts
  (y, table) = graph ! pt

getFile :: IO Reactions
getFile = parseFromFile (many1
    reaction) "ins.txt" >>= \case
  Left err -> print err >> pure empty
  Right inst -> pure $ fromList inst

reaction :: Parser (Element, Table)
reaction = do
  body <- pair `sepBy` string ", "
  (x, name) <- string " => " *> pair
  endOfLine >> pure (name, (x, body))

pair :: Parser Component
pair = do
  coeff <- read <$> many1 digit
  name <- space *> many1 letter
  return (coeff, name)
