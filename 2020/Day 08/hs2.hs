{-# LANGUAGE PartialTypeSignatures, BlockArguments #-}
import qualified Data.Vector as V
import qualified Data.Set as S
import Control.Monad.State
import Control.Lens
import Text.Printf
import Data.Maybe

type Tape = V.Vector (String, Int)
type Active = (Int, Int, S.Set Int)

main :: IO ()
main = do
  tape <- input
  printf "Silver: %d\n" (fst $eval tape `evalState`
    start) >> printf "Gold: %d\n" (repair tape)
start = (0, 0, S.empty)

repair :: Tape -> Int
repair xs = fst.fromJust.V.find snd $do
  (i, x) <- V.zip (V.enumFromN 0 $length xs) xs
  pure $evalState (eval $fn i x) start where
    fn i ("jmp", v) = xs &ix i .~ ("nop", v)
    fn i ("nop", v) = xs &ix i .~ ("jmp", v)
    fn i x = xs

eval :: Tape -> State Active (Int, Bool)
eval xs = do
  (acc, idx, seen) <- get
  if S.member idx seen then pure (acc, False) else do
    let (code, x) = xs V.! idx
    let acc' = (acc+) if code == "acc" then x else 0
    let idx' = (idx+) if code == "jmp" then x else 1
    let seen' = S.insert idx seen
    put (acc', idx', seen') >> if idx >= V.length
      xs then pure (acc, True) else eval xs

input :: IO Tape
input = V.fromList.map (fn.words).lines <$> readFile "input.txt" where
  gn ('+': xs) = read xs; gn v = read v; fn [c, v] = (c, gn v)
