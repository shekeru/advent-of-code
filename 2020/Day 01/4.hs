main :: IO ()
main = do
  fn <- solve.map read.lines <$> readFile "input.txt"
  let puts w i = mapM_ putStr [w, ": ", show $fn i, "\n"]
  puts "Silver" 2 >> puts "Gold" 3

solve :: [Int] -> Int -> Int
solve = (snd.head.filter ((== 2020).fst).map (\v -> (sum v, product v)) <$>).fn where
  fn _ 0 = [[]]; fn [] _ = []; fn (x:xs) r = ((x:) <$> fn xs (r-1)) <> fn xs r
