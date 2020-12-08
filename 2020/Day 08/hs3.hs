{-# LANGUAGE PartialTypeSignatures, BlockArguments #-}
import qualified Data.Vector as V
import qualified Data.Set as S
import Control.Monad.State
import Control.Lens
import Text.Printf
import Data.Either
import Data.Maybe
import Data.List

type Tape = V.Vector (String, Int)
type Active = (Int, Int, S.Set Int)

main :: IO ()
main = do
  tape <- input
  printf "Silver: %d\n" (fromLeft 0 $eval tape `evalState` start)
  printf "Gold: %d\n" $repair tape
start = (0, 0, S.empty)

repair :: Tape -> Int
repair xs = fromRight 0.fromJust.V.find isRight $V.zip xs (V.enumFromN
  0 $length xs) >>= pure.(`evalState` start).eval.uncurry fn where
    fn ("jmp", v) = (xs&).(.~ ("nop", v)).ix; fn ("nop", v) =
      (xs&).(.~ ("jmp", v)).ix; fn pair = const xs

eval :: Tape -> State Active (Either Int Int)
eval xs = do
  (acc, idx, seen) <- get; let (code, x) = xs V.! idx
  if S.member idx seen then pure (Left acc) else do
    let acc' = (acc+) if code == "acc" then x else 0
    let idx' = (idx+) if code == "jmp" then x else 1
    if idx >= V.length xs then pure (Right acc) else
      put (acc', idx', S.insert idx seen) >> eval xs

input :: IO Tape
input = V.fromList.map (fn.words).lines <$> readFile
  "input.txt" where fn [c, v] = (c, read $delete '+' v)
