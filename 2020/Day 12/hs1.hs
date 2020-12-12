import Control.Applicative
import Data.Function
import Data.Complex
import Text.Printf

type Action = (Char, Coordinate)
type Coordinate = Complex Float
type State = (Coordinate, Coordinate, Coordinate, Coordinate)

main :: IO ()
main = do
  (p1, p2, _, _) <- foldl step (0 :+ 0, 0 :+ 0, 1 :+ 0, 10 :+ 1) <$> input
  on (printf "Silver: %d\nGold: %d\n") (fn :: Coordinate -> Int) p1 p2
    where fn = liftA2 (fmap round.on (+) abs) realPart imagPart

step :: State -> Action -> State
step (a, b, h, w) x = f x (d x a, b, r x h, d x $r x w) where

f :: Action -> State -> State
f ('F', v) (a, b, h, w) = (a + v * h, b + v * w, h, w)
f _ st = st

d :: Action -> Coordinate -> Coordinate
d (c, v) p = p + v * fn c where
  fn 'N' = (0 :+ 1)
  fn 'E' = (1 :+ 0)
  fn 'W' = ((-1) :+ 0)
  fn 'S' = (0 :+ (-1))
  fn _ = (0 :+ 0)

r :: Action -> Coordinate -> Coordinate
r (c, v) p = p * (fn c) ** (v/90) where
  fn 'R' = (0 :+ (-1))
  fn 'L' = (0 :+ 1)
  fn _ = (1 :+ 0)

input :: IO [Action]
input = map (\(x:xs) -> (x, (read xs :+ 0)))
  .lines <$> readFile "input.txt"
