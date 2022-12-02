import Data.List
import Data.Function
import Text.Printf

main = sortBy (flip compare).map (\xs -> sum [read x |x <- xs, not $ null x])
    .groupBy (on (==) null).lines <$> readFile "input.txt" >>= \(elves :: [Int]) ->
    let solve = sum.(`take` elves) in on(printf "Silver: %d\nGold: %d\n") solve 1 3
