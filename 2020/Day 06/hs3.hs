import Data.Function (on)
import Data.List.Split (splitOn)
import Data.List (union, intersect)
import Control.Arrow ((&&&))
import Text.Printf (printf)

main :: IO ()
main = map lines.splitOn "\n\n" <$> readFile "input.txt"
  >>= uncurry (printf "Silver: %d\nGold: %d\n").on
  (&&&) ((sum.).map.(length.).foldl1) union intersect
