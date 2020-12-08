{-# LANGUAGE PartialTypeSignatures, TemplateHaskell #-}
import qualified Data.Vector as V
import qualified Data.Set as S
import Control.Lens.At
import Control.Lens
import Text.Printf
import Data.Maybe
import Data.List
import Data.Char

data State = State {
  _acc :: Int, _idx :: Int,
  _past :: S.Set Int
} deriving (Show)
type Tape = V.Vector (OpCode Int)
data OpCode v = Acc v | Jmp v | Nop v
  deriving (Show, Eq, Read)
makeLenses ''State

main :: IO ()
main = do
  tape <- input
  printf "Silver: %d\n"$ eval tape start
  printf "Gold: %d\n"$ negate$ fix tape
start = State 0 0 S.empty

fix :: Tape -> Int
fix xs = fromJust.V.find (<0)$ do
  (i, x) <- V.zip (V.enumFromN 0$ length xs) xs
  pure$ eval (fn i x) start where
    fn i (Jmp v) = xs &ix i .~ Nop v
    fn i (Nop v) = xs &ix i .~ Jmp v
    fn i x = xs

eval :: Tape -> State -> Int
eval xs st = if _idx st' >= V.length xs then (- _acc st') else
    if _idx st' `S.member` _past st then _acc st' else eval xs st' where
  st' = ((past %~) =<< S.insert . _idx).(idx +~ 1)$ case xs V.! _idx st of
      Jmp v -> st &idx +~ v - 1; Acc v -> st &acc +~ v; Nop _ -> st

input :: IO Tape
input = V.fromList.map fn.lines <$> readFile "input.txt" 
  where fn (x:xs) = read$ toUpper x : delete '+' xs
