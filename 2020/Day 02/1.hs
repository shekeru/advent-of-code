import Data.Functor
import Control.Arrow
import Data.List.Split
import Text.Printf
import Data.List

type Entry = ([Int], Char, String)

main :: IO ()
main = do
  solve <- input <&> fmap (length.filter id).flip map
  let puts str = printf (str <> ": %d\n").solve
  puts "Silver" silver >> puts "Gold" gold

silver :: Entry -> Bool
silver ([a, b], ch, pwd) = a <= v && v <= b
  where v = length $filter (== ch) pwd

gold :: Entry -> Bool
gold (ix, ch, pwd) = (== 1) $length $filter (uncurry
  (&&) <<< (`elem` ix) *** (== ch)) $zip [1..] pwd

input :: IO [Entry]
input = readFile "input.txt" <&> map (fn.words).lines where
  fn [a, b, c] = (map read $splitOn "-" a, head b, c)
