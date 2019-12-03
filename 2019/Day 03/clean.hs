import Data.Function (on)
import Data.List (mapAccumL)
import Data.List.Split (splitOn)
import Text.Printf (printf)

type Line = [Point]
data Point = Point {
  cVar :: Int,
  dMin :: Int,
  dMax :: Int,
  total :: Int,
  delta :: Int,
  plane :: Bool
} deriving Show

main :: IO()
main = do
  wires <- sequence <$> input
  let yss = filter cross wires
  printf "Silver: %d\n"
    (minimum $ part1 <$> yss)
  printf "Gold: %d\n"
    (minimum $ part2 <$> yss)

part1 :: Line -> Int
part1 = sum.map (abs.cVar)

part2 :: Line -> Int
part2 ll@[a,b] = base + fn a b + fn b a where
  fn x y = abs (cVar x - start y) where
    start = if delta y >= 0 then dMin else dMax
  base = sum $ map total ll

cross :: Line -> Bool
cross [a, b] = on (/=) plane a b && ll a b && ll b a
  where ll x y = dMin x <= cVar y && cVar y <= dMax x

input :: IO [Line]
input = map acc.lines <$> readFile "input.txt" where
  fn (x, y, t) (v:vs) = let i = read vs in case v of
    'R' -> ((x + i, y, t+i), Point y x (x+i) t i True)
    'L' -> ((x - i, y, t+i), Point y (x-i) x t (-i) True)
    'U' -> ((x, y+i, t+i), Point x y (y+i) t i False)
    'D' -> ((x, y-i, t+i), Point x (y-i) y t (-i) False)
  acc = snd.mapAccumL fn (0, 0, 0).splitOn ","
