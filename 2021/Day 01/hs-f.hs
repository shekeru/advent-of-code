import Text.Printf
import Data.Function
import Control.Applicative


main :: IO ()
main =  on (liftA2 $printf "Silver: %d\nGold: %d\n")
  ((length.filter (uncurry (>)) <$>).(>>= zip).drop) 1 3
  =<< (map read.lines <$> readFile "i1.txt" :: IO [Int])
