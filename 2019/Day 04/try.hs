import Text.Printf
import Control.Applicative
import Data.List

main :: IO()
main = do
  let fn = liftA2 (&&) (nub >>= (/=)) (sort >>= (==))
  let xs = filter fn $map show [136760..595730]
  printf "Silver: %d\n" $length xs
  printf "Gold: %d\n" $length $filter
    (elem 2.map length.group) xs
