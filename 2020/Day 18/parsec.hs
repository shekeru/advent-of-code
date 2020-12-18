{-# LANGUAGE PartialTypeSignatures, LambdaCase #-}

import Text.Printf
import Text.Parsec.String
import Text.Parser.Expression
import Text.Parser.Token.Style
import Text.Parser.Token
import Control.Monad
import Control.Applicative
import Data.List

main :: IO ()
main = mapM ((show.sum <$>).eval) [pure.concat, id] >>= zipWithM_
  (\x y -> putStrLn $intercalate ": " [x, y]) ["Silver", "Gold"]

eval :: _ -> IO [Integer]
eval alter = parseFromFile (many expr) "input.txt" >>= esc where
  esc = \case Left err -> print err >> pure []; Right values -> pure values
  expr = buildExpressionParser table $parens expr <|> natural
  op str fn = Infix (fn <$ reserve emptyOps str) AssocLeft
  table = alter [[op "+" (+)], [op "*" (*)]]
