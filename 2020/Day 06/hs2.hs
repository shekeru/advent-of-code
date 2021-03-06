import Data.Function (on)
import Data.List.Split (splitOn)
import Data.List (union, intersect)
import Control.Applicative (liftA2)
import Text.Printf (printf)

main :: IO ()
main = map lines.splitOn "\n\n" <$> readFile "input.txt"
  >>= on (liftA2 $printf "Silver: %d\nGold: %d\n")
  ((sum.).map.(length.).foldl1) union intersect
