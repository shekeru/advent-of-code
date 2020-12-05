import Text.Printf

main :: IO ()
main = do
  seats <- map (foldl (flip ((+).fromEnum.(`elem` "BR")).(*2)) 0).lines <$> readFile "input.txt"
  printf "Silver: %d\n" (maximum seats) >> printf "Gold: %d\n" (gauss seats - sum seats)
    where gauss x = div (maximum x * (maximum x + 1) - (minimum x - 1) * minimum x) 2
