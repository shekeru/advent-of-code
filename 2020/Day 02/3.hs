import Data.Functor
import Data.Function
import Control.Applicative
import Data.List.Split
import Text.Printf

main :: IO ()
main = do
  solve <- input <&> fmap (length.filter id).flip map
  let puts str = printf (str <> ": %d\n").solve
  puts "Silver" silver >> puts "Gold" gold

silver :: Entry -> Bool
silver ([a, b], ch, pwd) = liftA2 (&&) (a <=)
  (<= b) v where v = length $filter ch pwd

gold :: Entry -> Bool
gold ([a, b], ch, pwd) = on (/=) fn a b
  where fn = ch.(pwd !!).subtract 1

input :: IO [Entry]
input = readFile "input.txt" <&> map (fn.words).lines where
  fn [a, b, c] = (map read $splitOn "-" a, (==) $head b, c)

type Entry = ([Int], Char -> Bool, String)
