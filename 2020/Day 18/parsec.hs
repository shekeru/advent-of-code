{-# LANGUAGE PartialTypeSignatures, LambdaCase #-}

import Data.Function (on)
import Control.Applicative (many, (<|>))
import Text.Parsec.String (Parser, parseFromFile)
import Text.Parser.Token (parens, reserve, decimal)
import Text.Parser.Token.Style (emptyOps)
import Text.Parser.Expression
import Text.Printf (printf)

main :: IO ()
main = eval (pure.concat) >>= (eval id >>=)
  .on (printf "Silver: %d\nGold: %d\n") sum

eval :: _ -> IO [Integer]
eval fn = parseFromFile (many $expr fn) "input.txt" >>= \case
  Left err -> print err >> pure []; Right values -> pure values

expr :: ([[_]] -> [[_]]) -> Parser Integer
expr fn = buildExpressionParser (fn [[op "+" (+)], [op "*" (*)]]) $parens (expr fn)
  <|> decimal where op str fn = Infix (fn <$ reserve emptyOps str) AssocLeft
