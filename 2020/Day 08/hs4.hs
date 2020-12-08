{-# LANGUAGE PartialTypeSignatures, BlockArguments #-}
import qualified Data.Vector as V
import qualified Data.Set as S
import Control.Monad.State
import Control.Lens
import Text.Printf
import Data.List

type Tape = V.Vector (String, Int)
type Active = (Int, Int, S.Set Int, [Int])

main :: IO ()
main = do
  tape <- (`evalState` start) . eval <$> input
  printf "Silver: %d\n" (-1 * head tape)
  printf "Gold: %d\n" (head $filter (>0) tape)
start = (0, 0, S.empty, [])

eval :: Tape -> State Active [Int]
eval xs = do
  st@(acc, idx, seen, opts) <- get; let (fn', (code, x)) = (eval $xs &ix idx %~ g, xs V.! idx)
  let opts' = ($opts) if code /= "acc" then (head (evalState fn' st):) else id
  if S.member idx seen then pure (-acc:opts) else do
    let acc' = (acc+) if code == "acc" then x else 0
    let idx' = (idx+) if code == "jmp" then x else 1
    if idx >= V.length xs then pure [acc] else put
     (acc', idx', S.insert idx seen, opts') >> eval xs where
        g ("jmp", v) = ("nop", v); g ("nop", v) = ("jmp", v)

input :: IO Tape
input = V.fromList.map (fn.words).lines <$> readFile
  "input.txt" where fn [c, v] = (c, read $delete '+' v)
