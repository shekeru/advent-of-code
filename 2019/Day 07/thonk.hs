import Data.List
import Data.List.Split
import Data.Function
import Control.Lens
import Text.Printf

type Program = [Int]
type Output = [Int]
type Input = [Int]

main :: IO()
main = do
  signal <- map.loop.eval 0 <$> input
  let solve = maximum.signal.permutations
  let puts x = printf (x <> ": %d\n").solve
  puts "Silver" [0..4]; puts "Gold" [5..9]

loop :: (Input -> Output) -> Input -> Int
loop amp [a,b,c,d,e] =
  last e' where
    a' = amp $a:0 :e'
    b' = amp $b :a'
    c' = amp $c :b'
    d' = amp $d :c'
    e' = amp $e :d'

eval :: Int -> Program -> Input -> Output
eval idx tape ins = case op of
  8 -> uncurry eval (cmp (==)) ins
  7 -> uncurry eval (cmp (<)) ins
  6 -> eval (jmp (==)) tape ins
  5 -> eval (jmp (/=)) tape ins
  4 -> val 1: eval (2 +idx) tape ins
  3 -> eval (2 +idx) tape' $tail ins
    where tape' = tape & ix (frc 1) .~ head ins
  2 -> uncurry eval (int (*)) ins
  1 -> uncurry eval (int (+)) ins
  99 -> mempty; where
    cmp fn = int(\x y -> fromEnum $fn x y)
    jmp fn = if fn (val 1) 0 then val 2 else idx + 3
    int fn = (idx + 4, tape & ix (frc 3) .~ on fn val 1 2)
    val n = let y = frc n in if im !! (n - 1) then y else tape !!y
    (op, im) = (\x -> (mod x 100, odd.(`mod` 10).div x <$>
      [100, 1000])) $tape !!idx; frc = (tape!!).(+idx)

input :: IO Program
input = map read.splitOn ","
  <$> readFile "input.txt"
