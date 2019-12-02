{-#LANGUAGE QuasiQuotes #-}

import Data.Function (on)
import Control.Lens hiding (re)
import Data.Vector hiding (map, zip)
import Control.Lens.At (iix)
import Text.RE.TDFA.String
import Text.Printf

main :: IO()
main = do
  xs <- input
  printf "Silver: %d\n"
    $ eval xs [12, 2]
  printf "Gold: %d\n"
    $ values xs

values :: Vector Int -> Int
values xs = 100 * n + v where
  (n, v) = divMod t $
    eval xs [1, 0] - b
  t = 19690720 - b
  b = eval xs [0, 0]

eval :: Vector Int -> [Int] -> Int
eval arr nv = run 0 $arr // zip [1..] nv where
  run k xs = case zx of
    99 -> unsafeHead xs; 2 -> op (*); 1 -> op (+); where
      op fn = run (k + 4) (xs & iix c .~ on fn (xs!) a b)
      [zx, a, b, c] = toList $ slice k 4 xs

input :: IO (Vector Int)
input = fromList.regex <$> readFile "input.txt" where
  regex = map read.matches.(*=~ [re|@{%int}|])
