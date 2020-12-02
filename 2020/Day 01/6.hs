import Control.Recursion
import Text.Printf

main :: IO ()
main = do
  nums <- map read.lines <$> readFile "input.txt"
  printf "Silver: %d\n" $head $sch 2020 nums
  printf "Gold: %d\n" $part2 nums

sch :: Int -> [Int] -> [Int]
sch goal = para fn where
    fn Nil = []; fn (Cons x (past, xs)) = case filter
      ((== goal).(+x)) past of (y:_) -> x * y : xs; _ -> xs

part2 :: [Int] -> Int
part2 nums = head $concatMap fn nums where
  fn a = fmap (*a) $sch (2020 - a) nums
