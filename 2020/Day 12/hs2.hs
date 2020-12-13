{-# LANGUAGE BlockArguments #-}
import Control.Applicative
import Data.Function
import Data.Complex
import Text.Printf

type Action = (Char, Coordinate)
type Coordinate = Complex Float
type State = (Coordinate, Coordinate, Coordinate, Coordinate)

main :: IO ()
main = do
  (p1, p2, _, _) <- foldl step (0 :+ 0, 0 :+ 0, 1 :+ 0, 10 :+ 1) <$>
    map (\(x:xs) -> (x, (read xs :+ 0))).lines <$> readFile "input.txt"
  on (printf "Silver: %d\nGold: %d\n") (fn :: Coordinate -> Int) p1 p2
    where fn = liftA2 (fmap round.on (+) abs) realPart imagPart

step :: State -> Action -> State
step (a, b, h, w) (c, v) = f (d a, b, r h, d $r w) where
  f z@(a, b, h, w) = case c of
    'F' -> (a + v * h, b + v * w, h, w); _ -> z
  r p = p * (** (v/90)) case c of
    'R' -> (0 :+ (-1)); 'L' -> (0 :+ 1); _ -> (1 :+ 0)
  d p = p + v * case c of
    'N' -> (0 :+ 1); 'S' -> (0 :+ (-1))
    'E' -> (1 :+ 0); 'W' -> ((-1) :+ 0)
    _ -> (0 :+ 0)
