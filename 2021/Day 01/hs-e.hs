import Text.Printf
import Control.Monad

main :: IO ()
main = do
  input <- map read.lines <$> readFile "i1.txt"
  let putf str fn = printf str (solve $ fn input)
  putf "Silver: %d\n" id >> putf "Gold: %d\n" (window 3)

solve :: [Int] -> Int
solve = length.filter (uncurry (<)).ap zip tail

window :: Int -> [Int] -> [Int]
window k xs | k > length xs = mempty
  | otherwise = sum (take k xs) : window k (tail xs)
