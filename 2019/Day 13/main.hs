import Data.List; import Data.List.Split
import Data.Function; import Text.Printf
import qualified Data.Vector as V; import IntCode
import Data.Vector (Vector, indexed, (!), (//))

main :: IO()
main = do
  tape <- input :: IO (Vector Int)
  let scan vx (i, x) = 3 == x && on (&&) ((== 0).(vx!)) (i-1) (i+1)
  let unit = fst $V.head $V.filter (scan tape) (indexed tape)
  let tape' = (0, 2): zip [unit - 17..unit + 17] (repeat 3)
  printf "Silver: %d\n" $length$filter (== 2) $map last$chunksOf
    3$fn tape; printf "Gold: %d\n" $last(fn $tape // tape')
  where fn xvs = eval (Program 0 0 xvs) (repeat 0)
