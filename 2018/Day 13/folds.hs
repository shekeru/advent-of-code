module Main where

import qualified Data.Map.Strict as SM
import Prelude hiding (Left, Right)
import Data.List (mapAccumL)
import Text.Printf

data Direction = Crash | North | East | South | West deriving (Show, Eq)
type Carts = SM.Map Coords Cart; type Tracks = [String]
type Coords = (Int, Int); type Cart = (Direction, Turn)
data Turn = Left | Ahead | Right deriving (Show, Eq)

input :: IO (Tracks, Carts)
input = do
  xss <- lines <$> readFile "input.txt"
  let parse (y,_,c) = mapAccumL addCart (y+1, 0, c)
  let ((_,_, carts), tracks) = mapAccumL parse (-1, 0, SM.empty) xss
  return (tracks, carts)

main :: IO ()
main = do
  (tracks, carts) <- input; let states = iterate (runSystem tracks) carts; crashed f = SM.filter (\(d,t) -> d `f` Crash)
  let [(y1,x1), (y2,x2)] = [\(f, g) -> (fst.head.head.dropWhile g) $map (SM.assocs.crashed f) states] <*> [((==), null), ((/=),(<) 1.length)]
  printf "Silver: First impact at %d,%d\n" x1 y1; printf "Gold: Last cart at %d,%d\n" x2 y2

runSystem :: Tracks -> Carts -> Carts
runSystem tracks x = SM.foldlWithKey (stepSystem tracks) x x

addCart :: (Int, Int, Carts) -> Char -> ((Int, Int, Carts), Char)
addCart acc '>' = (extract acc East, '-'); addCart acc '<' = (extract acc West, '-')
addCart acc '^' = (extract acc North, '|'); addCart acc 'v' = (extract acc South, '|')
addCart (y, x, carts) c = ((y, x+1, carts), c)

extract :: (Int, Int, Carts) -> Direction -> (Int, Int, Carts)
extract (y, x, carts) dir = (y, x+1, SM.insert (y, x) (dir, Left) carts)

stepSystem :: Tracks -> Carts -> Coords -> Cart -> Carts
stepSystem tracks carts k@(y,x) meta = if (carts SM.! k) /= (Crash, Ahead) then
  SM.insertWithKey collide pos' meta' carts' else carts' where
  (pos', meta') = discern (tracks!!y!!x) k meta
  carts' = SM.delete k carts

collide :: Coords -> Cart -> Cart -> Cart
collide crds cart (Crash, _) = cart
collide crds _ _ = (Crash, Ahead)

discern :: Char -> Coords -> Cart -> (Coords, Cart)
discern chr pos cart = (apply dir' pos, l)
  where l@(dir', t) = align chr cart

align :: Char -> Cart -> Cart
align _ (Crash, t) = (Crash, t)
-- No Changes
align '|' cart = cart; align '-' cart = cart;
align '+' (dir, Ahead) = (dir, Right)
-- Intersection Left
align '+' (North, Left) = (West, Ahead)
align '+' (West, Left) = (South, Ahead)
align '+' (South, Left) = (East, Ahead)
align '+' (East, Left) = (North, Ahead)
-- Intersection Right
align '+' (North, Right) = (East, Left)
align '+' (East, Right) = (South, Left)
align '+' (South, Right) = (West, Left)
align '+' (West, Right) = (North, Left)
-- Corner 2
align '\\' (North, t) = (West, t)
align '\\' (West, t) = (North, t)
align '\\' (South, t) = (East, t)
align '\\' (East, t) = (South, t)
-- Corner 1
align '/' (North, t) = (East, t)
align '/' (East, t) = (North, t)
align '/' (South, t) = (West, t)
align '/' (West, t) = (South, t)

apply :: Direction -> Coords -> Coords
apply North (y, x) = (y-1, x)
apply South (y, x) = (y+1, x)
apply West (y, x) = (y, x-1)
apply East (y, x) = (y, x+1)
apply Crash coords = coords
