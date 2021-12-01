import Text.Printf
import Data.Function
import Control.Monad

main :: IO ()
main = (map sum.window 3 >>= flip
  (printf "Silver: %d\nGold: %d\n" `on` solve))
  =<< map read.lines <$> readFile "i1.txt" where
    solve = length.filter (uncurry (<)).ap zip tail

window :: Int -> [Int] -> [[Int]]
window k xs | k > length xs = []
  | otherwise = take k xs : window k (tail xs)
