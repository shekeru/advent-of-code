import Text.Printf (printf)

main :: IO ()
main = do
  fn <- solve.map read.lines
    <$> readFile "input.txt"
  printf "Silver: %d\n" $fn 2
  printf "Gold: %d\n" $fn 3

solve :: [Int] -> Int -> Int
solve = (.) (snd.head.filter ((== 2020).fst).map
  (\v -> (sum v, product v))) <$> ($).fn where
    fn _ 0 = [[]]; fn [] _ = []; fn (x:xs) r =
      [x:ys | ys <- fn xs $r -1] <> fn xs r
