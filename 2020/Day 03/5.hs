import Control.Monad
import Text.Printf

main :: IO ()
main = sequence (solve <$> slopes) <$> (map cycle.lines <$> readFile "input.txt")
  >>= liftM2 (>>) (printf "Silver: %d\n".(!! 1)) (printf "Gold: %d\n".product)
    where slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

solve :: (Int, Int) -> [String] -> Int
solve (x, y) ix = length $ [0, y..length ix - 1] >>= guard.(=='#').
  ((`mod` 31).(*x).(`div` y) >>= flip ((!!).(!!) ix)) >> pure Nothing
