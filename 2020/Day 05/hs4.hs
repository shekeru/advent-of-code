import Text.Printf

main :: IO ()
main = do
  seats <- map (foldl (flip ((+).fromEnum.(`elem` "BR")).(*2)) 0).lines <$> readFile "input.txt"
  printf "Silver: %d\n" (maximum seats) >> printf "Gold: %d\n" (result seats) where
    result x = (length x + 1) * (2 * maximum x - length x) `div` 2 - sum x
