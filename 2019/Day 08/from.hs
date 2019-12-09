import Data.Function
import Data.List.Split
import Text.Printf
import Data.Maybe
import Data.List
import Data.Ord

main :: IO()
main = do
  xvs <- chunksOf 150.init <$> readFile "ins.txt"
  let min = minimumBy (comparing $fn '0') xvs
  printf "Silver: %d\n" $on (*) (`fn` min) '1' '2'
  putStrLn.intercalate "\n".chunksOf 25 $op.fromJust.
    find ('2' /=) <$> transpose xvs where
      fn = (.)length.filter.(==)
      op '0' = ' '; op '1' = '■'
