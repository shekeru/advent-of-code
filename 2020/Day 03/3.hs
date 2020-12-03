import Text.Printf

main :: IO ()
main = do
  let slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
  trees <- sequence (solve <$> slopes) <$> input
  printf "Silver: %d\n" $trees !!1
  printf "Gold: %d\n" $product trees

solve :: (Int, Int) -> [[Int]] -> Int
solve (x, y) w@(h:_) = sum $uncurry (!!) <$> zip (map (w!!)
  [0, y..length w - 1]) ((`mod` length h) <$> [0, x..])

input :: IO [[Int]]
input = map ((fromEnum.(== '#')) <$>)
  .lines <$> readFile "input.txt"
