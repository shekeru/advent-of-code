{-# LANGUAGE BlockArguments #-}
import Data.Array.ST
import Control.Monad.ST
import Control.Monad
import Data.Function
import Text.Printf

main :: IO ()
main = 30000000 &on (printf "Silver: %d\nGold: %d\n")
  (turn $(,) <*> length $zip [1,2,16,19,18,0] [1..]) 2020

turn :: ([(Int, Int)], Int) -> Int -> Int
turn (xs, t) nth = runST do
  vref <- newArray (0, nth) 0 :: ST s (STUArray s Int Int)
  forM_ xs $writeArray vref &uncurry
  flip (`foldM` 0) [t+1..nth-1] \c t -> do
    v <- readArray vref c; writeArray vref c t
      >> pure if v /= 0 then t - v else 0
