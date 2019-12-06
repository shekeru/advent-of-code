import Data.Function (on)
import Text.Printf (printf)
import Data.List.Split (splitOn)
import Data.Map.Strict hiding (foldl,
  fromList, (\\), union)
import Data.Set (fromList, (\\), union)
import Prelude hiding (lookup, insert)
type Graph = Map String String

main :: IO()
main = do
  sys <- (\s -> mapWithKey (\k _
    -> flatten s k) s) <$> input
  printf "Silver: %d\n" $foldl
    (\s x -> s + length x) 0 sys
  printf "Gold: %d\n" $length $on
    (\x y -> union (x\\y) $y\\x)
    (fromList.(!)sys) "SAN" "YOU"

flatten :: Graph -> String -> [String]
flatten xvs k = case lookup k xvs of
  Just v -> v : flatten xvs v
  Nothing -> mempty

input :: IO Graph
input = foldl fn empty.lines
  <$> readFile "input.txt" where
  fn xvs ln = insert ch pr xvs
    where [pr, ch] = splitOn ")" ln
