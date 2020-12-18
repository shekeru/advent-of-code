import Control.Monad
import qualified Data.Set as Set
import Data.Function
import Text.Printf

type Position = [Int]
type Grid = (Set.Set Position)

main :: IO ()
main = input >>= on (printf "Silver: %d\nGold: %d\n")
  (length.(!! 6).iterate step) <*> Set.map (0:)

step :: Grid -> Grid
step v = Set.foldl' kill v v where
  factor = foldl (\s y -> s + fromEnum (Set.member y v)) 0
  kill av x = let nodes = nearby x in foldl spawn (if liftM2 (||)
    (== 2) (== 3) $factor nodes then av else Set.delete x av) nodes
  spawn av x = if factor (nearby x) == 3 then Set.insert x av else av

nearby :: Position -> [Position]
nearby x = zipWith (+) x <$> tail(replicateM (length x) [0, 1, -1])

input :: IO Grid
input = Set.fromList.concatMap fn.zip [0..].lines <$> readFile "input.txt"
  where fn (y, xs) = [[y, x, 0] | (x, t) <- zip [0..] xs, t == '#']
