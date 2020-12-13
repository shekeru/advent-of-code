{-# LANGUAGE LambdaCase, PartialTypeSignatures, BlockArguments #-}
import qualified Data.Map.Strict as SM
import Control.Monad.State
import Control.Monad
import Text.Printf
import Data.Maybe
import Data.List

type Pos = (Int, Int)
type Tile = Maybe Bool
type Seats = SM.Map Pos Tile

main = do
  simulate <- solve <$> input
  printf "Silver: %d\n" $simulate 4
  printf "Gold: %d\n" $simulate 5

solve :: Seats -> Int -> Int
solve xs n = step `evalState` (0, xs) where
  step = do
    (c, v) <- get
    let v' = SM.mapWithKey (fn v) v
    let c' = count v'
    if c == c' then pure c else put (c', v') >> step where
      fn v k (Just True) = Just if factor n v k >= n then False else True
      fn v k (Just False) = Just if factor n v k /= 0 then False else True
      fn v k x = x

count :: Seats -> Int
count = foldl ((.(\case Just True -> 1; _ -> 0)).(+)) 0.SM.elems

factor :: Int -> Seats -> Pos -> Int
factor n v pt = length $filter id $map seek $tail $replicateM 2 [0, 1, -1] where
  seek [a, b] = fuck n $seek' pt where
    fuck 4 = maybe False (\case Just x -> x; _ -> False).find (const True)
    fuck 5 = maybe False fromJust.find isJust
    seek' (x, y) = let pt' = (x+a, y+b) in
      case SM.lookup pt' v of
        Just t -> t:seek' pt'
        Nothing -> []

input :: IO Seats
input = SM.fromList.concatMap(\(y, xs) -> zip (zip [0..] $repeat y) $map (\case
  'L' -> Just False; '.' -> Nothing) xs).zip [0..].lines <$> readFile "input.txt"
