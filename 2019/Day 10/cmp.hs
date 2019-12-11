import Text.Printf
import Data.Function
import Control.Applicative
import Control.Arrow
import Data.Complex
import Data.Tuple
import Data.List
import Data.Ord

type Point = Complex Float
type Polar = (Float, Float)

main :: IO()
main = do
  (pt, xvs) <- eval.pts <$> readFile "ins.txt"
  printf "Silver: %d\n" $length xvs; printf
    "Gold: %.f\n" $xvs!!199 `fixed` pt

fixed :: Polar -> Point -> Float
fixed = (+).uncurry mkPolar.swap.first negate >>>
  fmap (liftA2 (+) ((*100).imagPart) realPart)

eval :: [Point] -> (Point, [Polar])
eval xs = maximumBy (comparing $length.snd)
  $zip xs $nubBy (on (==) fst).sort.(>>=)
   (`delete` xs) (mapM calc) <$> xs where
  calc = (-) >>> fmap(first negate.swap.polar)

pts :: String -> [Point]
pts fs = [on (:+) fromIntegral y x
  | (y, ln) <- zip[0..] $lines fs,
  (x, c) <- zip[0..] $ln, c == '#']
