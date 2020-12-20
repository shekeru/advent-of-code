import Control.Monad
import qualified Data.Set as Set
import Data.Function
import Text.Printf

main :: IO ()
main = input >>= on (printf "Silver: %d\nGold: %d\n")
  (length.(!! 6).iterate step) <*> Set.map (0:)

step :: Grid -> Grid
step v = do
  let next_to = Set.fromList $concatMap nearby v
  let births = Set.filter ((== 3).factor) next_to
  let deaths = Set.filter (liftM2 (&&) (/= 2) (/= 3).factor) v
  Set.union (v Set.\\ deaths) births where
    nearby x = zipWith (+) x <$> tail (replicateM (length x) [0, 1, -1])
    factor = foldl (\s y -> s + fromEnum (Set.member y v)) 0.nearby

input :: IO Grid; type Grid = (Set.Set [Int])
input = Set.fromList.concatMap fn.zip [0..].lines <$> readFile "input.txt"
  where fn (y, xs) = [[y, x, 0] | (x, t) <- zip [0..] xs, t == '#']
