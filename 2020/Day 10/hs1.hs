import Text.Printf (printf)
import Data.List (sort)

main :: IO ()
main = do
  array <- sort.map read.lines
    <$> readFile "input.txt"
  printf "Silver %d\n" (whore array)
  printf "Gold: %d\n" (cunt array)

whore :: [Int] -> Int
whore = (\[_,a,_,b] -> a * b).foldl slut [0, 0, 0, 1] where
  slut z@(x:_) k = k : [fromEnum(o == k-x) + z!!o | o <- [1..3]]

cunt :: [Int] -> Int
cunt xs = piss (maximum xs) where
  piss = (map shit [0..] !!) where
    shit 0 = 1; shit v = if elem v xs then fuck else 0
      where fuck = sum [piss $v-o | o <- [1..3], v >= o]
