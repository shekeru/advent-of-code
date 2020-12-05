import Control.Applicative
import Text.Printf
import Data.List
import Data.Bits

main :: IO ()
main = map (foldl (\i c -> shift i 1 .|. fromEnum(elem c "BR")) 0).lines <$> readFile "input.txt"
  >>= liftA2 (printf "Silver: %d\nGold: %d\n") (maximum) (\x -> head $[minimum x..maximum x] \\ x)
