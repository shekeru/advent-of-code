import Data.Function
import Data.List.Split
import Text.Printf
import Data.List
import Data.Ord

main :: IO()
main = do
  xvs <- input $25 *6
  let min = minimumBy (comparing $fn '0') xvs
  printf "Silver: %d\nGold:" $on (*) (`fn` min) '1' '2'
  mapM_ (putStrLn.('\t':)) $chunksOf 25 $op
      <$> foldr1 (zipWith fd) xvs where
    fn = (.)length.filter.(==)
    op '0' = ' '; op '1' = '■'
    fd '2' b = b; fd t _ = t

input :: Int -> IO [String]
input ln = chunksOf ln.init
  <$> readFile "ins.txt"
