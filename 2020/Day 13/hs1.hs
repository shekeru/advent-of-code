import Control.Arrow
import Control.Monad
import Data.Function
import Text.Printf
import Data.List.Split
import Data.List

main :: IO ()
main = input >>= liftM2 (>>)
  (printf "Silver: %d\n".uncurry silver.second (map snd))
  (printf "Gold: %d\n".fst.foldl gold (0, 1).snd)

silver :: Int -> [Int] -> Int
silver n = uncurry (*).minimumBy
  (on compare snd).map (ap (,) $(-) <*> mod n)

gold :: (Int, Int) -> (Int, Int) -> (Int, Int)
gold (t, f) (i, x) = if mod (i + t) x /= 0
  then gold (t+f, f) (i, x) else (t, f*x)

input :: IO (Int, [(Int, Int)])
input = fn.lines <$> readFile "input.txt" where
  fn [n, xs] = (read n, filter ((/= 0).snd) $zip [0..]
    $map gn $splitOn "," xs); gn "x" = 0; gn x = read x
