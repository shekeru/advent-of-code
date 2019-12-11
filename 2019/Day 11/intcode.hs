{-# LANGUAGE TemplateHaskell #-}
module IntCode where

import Control.Lens
import Control.Lens.TH
import Data.List.Split
import Data.Function
import Data.Vector
  (Vector, fromList, (!))

data Program = Program {
  _idx :: Int, _rbx :: Int,
  _tape :: Vector Int
} deriving Show
$(makeLenses ''Program)
type Output = [Int]
type Input = [Int]

eval :: Program -> Input -> Output
eval st@(Program i r t) ins = case op of
  9 -> flip eval ins $ st&idx +~ 2 &rbx +~ val(ptr 1)
  8 -> eval (cmp (==)) ins
  7 -> eval (cmp (<)) ins
  6 -> eval (jmp (==)) ins
  5 -> eval (jmp (/=)) ins
  4 -> val(ptr 1) :eval (st&idx +~ 2) ins
  3 -> flip eval (tail ins) $ st&idx +~ 2 &tape.ix(ptr 1) .~ head ins
  2 -> eval (int (*)) ins
  1 -> eval (int (+)) ins
  99 -> mempty; where
    cmp = int.(fmap fromEnum.)
    int fn = st&idx +~ 4 &tape.ix(ptr 3) .~ on fn(val.ptr) 1 2
    jmp fn = st&idx .~ if fn(val$ ptr 1) 0 then val(ptr 2) else 3+i
    (op, im) = (\x -> (mod x 100, (`mod` 10).div x.(10^)
      <$> [2,3,4]))$ val i; val = (t!)
    ptr n = let y = n + i in case im!!(n - 1) of
      2 -> r + val y; 1 -> y; 0 -> val y

input :: IO Program
input = Program 0 0.fromList.take 1250.(<> repeat 0)
  .map read.splitOn "," <$> readFile "ins.txt"
