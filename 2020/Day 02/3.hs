import Control.Applicative
import Data.List.Split
import Data.Function
import Data.Functor

main :: IO ()
main = do
  solve <- input <&> fmap (length.filter id).flip map
  let puts str = putStrLn.(str <> ": " ++).show.solve
  puts "Silver" silver >> puts "Gold" gold

input :: IO [Entry]; type Entry = ([Int], Char -> Bool, String)
input = readFile "input.txt" <&> map (fn.words).lines where
  fn [a, b, c] = (map read $splitOn "-" a, (==) $head b, c)

silver :: Entry -> Bool
silver ([a, b], ch, pwd) = liftA2 (&&)
  (a <=) (<= b) $length $filter ch pwd

gold :: Entry -> Bool
gold ([a, b], ch, pwd) = on (/=)
  (ch.(pwd !!).subtract 1) a b
