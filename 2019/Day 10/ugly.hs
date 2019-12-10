import Data.Function; import Data.List
import Text.Printf; import Data.Ord
import Data.Map.Strict
  (fromDescList, toAscList)

type Point = (Float, Float)
type Polar = Point

main :: IO()
main = do
  (pt, xvs) <- eval.pts <$> readFile "ins.txt"
  printf "Silver: %d\n" $length xvs; printf
    "Gold: %.f\n" $fixed pt $xvs!!199

eval :: [Point] -> (Point, [Polar])
eval xs = maximumBy (comparing $length.snd)$zip
  xs$toAscList.fromDescList.sortBy(flip compare)
  .(>>=) (`delete` xs) (flip$fmap.polar) <$> xs

fixed :: Point -> Polar -> Float
fixed (a, b) (th, r) = y + 100 * x where
  (x, y) = (r *sin(pi -th) +a, r *cos(pi -th) +b)

polar :: Point -> Point -> Polar
polar (x, y) (a, b) = let cf = (a - x, b - y) in (pi -
  uncurry atan2 cf, uncurry(fmap sqrt.(+) `on` (^2)) cf)

pts :: String -> [Point]
pts fs = [(fn x, fn y)|
  y <- zip[0..] $lines fs,
  x <- zip[0..] $snd y, snd x == '#']
    where fn = fromIntegral.fst
