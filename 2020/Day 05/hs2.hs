import Text.Printf

main :: IO ()
main = do
  seats <- map (foldl fn 0).lines <$> readFile "input.txt"
  printf "Silver: %d\n" (maximum seats) >> printf "Gold: %d\n"
    (sum [minimum seats..maximum seats] - sum seats) where
      fn a x = 2 * a + fromEnum (elem x "BR")
