{-# LANGUAGE PartialTypeSignatures, LambdaCase #-}
module Main where

import Data.Bits
import Data.Word
import Data.IORef
import System.IO.Unsafe
import Data.Map hiding (null)
import Text.Parsec hiding (State)
import Text.Parsec.String
import Text.Printf

main :: IO ()
main = do
  part1 <- eval mempty
  printf "Silver: %d\n" part1
  part2 <- eval $ modifyIORef'
    world (insert "b" part1)
  printf "Gold: %d\n" part2

eval :: IO () -> IO Word16
eval force = parseFromFile (many wires) "input.txt" >>= \case
  Right _ -> force >> pure (val "a")
  Left err -> print err >> pure 0

wires :: Parser String
wires = do
  left <- entry
  right <- string "-> " *>
    many1 lower <* endOfLine
  unsafePerformIO(modifyIORef' world $
    insert right left) `seq` pure right

entry :: Parser Word16
entry = do
  left <- value <* space <|> pure 0
  op <- many1 upper <* space <|> pure ""
  right <- value <* space <|> pure 0
  pure $ case op of
    "RSHIFT" -> left `shiftR` fromEnum right
    "LSHIFT" -> left`shiftL` fromEnum right
    "NOT" -> complement right
    "AND" -> left .&. right
    "OR" -> left .|. right
    _ -> left

value :: Parser Word16
value = read <$> many1 digit
  <|> val <$> many1 lower

val :: String -> Word16
val key = unsafePerformIO $
  (! key) <$> readIORef world

world :: IORef (Map String Word16)
world = unsafePerformIO (newIORef empty)
{-# NOINLINE world #-}
