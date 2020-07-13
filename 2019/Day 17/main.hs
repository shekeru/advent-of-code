import Data.Vector (Vector, toList, (!), (//))
import qualified Data.Set as S
import Data.List
import Text.Printf
import Data.Char
import IntCode

data Face = North | East | South | West
type Crds = (Int, Int)

main :: IO()
main = do
  tape <- input :: IO (Vector Int)
  let tape' = tape // [(0, 2)]
  let retStr = map chr (fn tape [])
  let path = pathed (lines retStr)
  let valid = intersects path
  printf "Silver: %d\n" $params valid
  printf "Gold: %d\n" $last $fn tape' solv
  where
    fn xvs = eval (Program 0 0 xvs)
    solv = map ord $ concat [
      "C,A,A,C,B,A,B,B,A,C\n",
      "R,8,L,6,L,6\n",
      "L,10,R,10,L,6\n",
      "R,10,R,8,L,10,L,10\n",
      "n\n"]

params :: [Crds] -> Int
params = sum.map mul where
  mul (y, x) = y * x

pathed :: [String] -> [Crds]
pathed xss = concatMap fix $
  zip [0..] (map assign xss)

intersects :: [Crds] -> [Crds]
intersects xss = [pos |
    pos <- S.elems set, all
    (`S.member` set) (nby4 pos)]
  where set = S.fromList xss

nby4 :: Crds -> [Crds]
nby4 (y, x) = [(y+1, x), (y-1, x), (y, x-1), (y, x+1)]

assign :: String -> [Int]
assign xs = [x | (x, c) <-
  zip [0..] xs, c == '#']

fix :: (Int, [Int]) -> [Crds]
fix (y, xs) = [(y, x) | x <- xs]
