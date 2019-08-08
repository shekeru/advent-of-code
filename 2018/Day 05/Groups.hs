import Data.Group
import Text.Printf
import Data.Algebra.Free
import Data.Group.Free
import Data.Char

main :: IO()
main = mapM_ (input >>=) [
   printf "part 1: %d\n".silver,
   printf "part 2: %d\n".minimum.map
    silver.(polymers <*>).pure
   ] where silver = length.toList

input :: IO (FreeGroupL Char)
input = foldMap inject.init
  <$> readFile "input.txt"

inject :: Char -> FreeGroupL Char
inject c = if isLower c then returnFree c
  else invert $ returnFree (toLower c)

polymers :: [FreeGroupL Char -> FreeGroupL Char]
polymers = map func ['a'..'z'] where
  func c = foldMapFree $ \x -> if x == c
    then mempty else returnFree x
