import Data.Function
import Control.Applicative
import Data.List.Split
import Text.Printf
import Data.List

main :: IO ()
main = map lines.splitOn "\n\n" <$> readFile "input.txt"
    >>= on (liftA2 $printf "Silver: %d\nGold: %d\n")
  ((sum.).map.(length.)) (nub.concat) (foldl1 intersect)
