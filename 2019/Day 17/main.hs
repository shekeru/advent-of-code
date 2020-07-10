import Data.Vector (Vector, toList, (!), (//))
import qualified Data.Set as S
import Text.Printf
import Data.Char
import IntCode

type Crds = (Int, Int)

main :: IO()
main = do
  tape <- input :: IO (Vector Int)
  let retStr = map chr (fn tape)
  let valid = intersects (lines retStr)
  printf "Silver: %d\n" $params valid
  putStrLn retStr
  where
    fn xvs = eval (Program 0 0 xvs) []

params :: [Crds] -> Int
params = sum.map mul where
  mul (y, x) = y * x

intersects :: [String] -> [Crds]
intersects xss = [pos |
    pos <- S.elems set, all
    (`S.member` set) (nby4 pos)]
  where
    idxd = zip [0..] (map assign xss)
    set = S.fromList (concatMap fix idxd)

nby4 :: Crds -> [Crds]
nby4 (y, x) = [(y+1, x), (y-1, x), (y, x-1), (y, x+1)]

assign :: String -> [Int]
assign xs = [x | (x, c) <-
  zip [0..] xs, c == '#']

fix :: (Int, [Int]) -> [Crds]
fix (y, xs) = [(y, x) | x <- xs]
