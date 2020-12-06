import Data.Function
import qualified Data.Set as S
import Control.Applicative
import Data.List.Split
import Text.Printf

main :: IO ()
main = map (map S.fromList.lines).splitOn "\n\n" <$> readFile
  "input.txt" >>= on (liftA2 $printf "Silver: %d\nGold: %d\n")
  ((sum.).map.(S.size.)) S.unions (foldl1 S.intersection)
