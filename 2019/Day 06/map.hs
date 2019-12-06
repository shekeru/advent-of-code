import Data.List ((\\))
import Data.Function (on)
import Text.Printf (printf)
import Data.List.Split (splitOn)
import qualified Data.Map.Strict as SM
type Graph = SM.Map String String

main :: IO()
main = do
  sys <- (\s -> SM.mapWithKey (\k _
    -> flatten s k) s) <$> input
  printf "Silver: %d\n" $foldl
    (\s x -> s + length x) 0 sys
  printf "Gold: %d\n" $length $on
    (\x y -> (x\\y) <> (y\\x))
    (sys SM.!) "SAN" "YOU"

flatten :: Graph -> String -> [String]
flatten xvs k = case SM.lookup k xvs of
  Just v -> v : flatten xvs v
  Nothing -> mempty

input :: IO Graph
input = foldl fn SM.empty.lines
  <$> readFile "input.txt" where
  fn xvs ln = SM.insert ch pr xvs
    where [pr, ch] = splitOn ")" ln
