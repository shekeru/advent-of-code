{-# LANGUAGE LambdaCase #-}
import Data.Function
import Data.List.Split
import Text.Printf
import Data.List
import Data.Ord

data Pixel = B | W | T
  deriving (Eq)

instance Read Pixel where
  readList str = [(read.pure <$> str, "")]
  readsPrec _ x = [(p $ head x, tail x)] where
    p = \case '2' -> T; '1' -> W; '0' -> B

instance Semigroup Pixel where
    T <> y = y; x <> _ = x

instance Show Pixel where
  showsPrec _ W = (:) '■'
  showsPrec _ _ = (:) ' '
  showList = fmap ('\t':)
    .foldr (fmap.shows) id

main :: IO()
main = do
  xvs <- input $25 *6
  let min = minimumBy (comparing $fn B) xvs
  printf "Silver: %d\nGold:" $on (*) (`fn` min) W T
  mapM_ print $chunksOf 25 $foldr1 (zipWith (<>)) xvs
    where fn = fmap length.filter.(==)

input :: Int -> IO [[Pixel]]
input ln = chunksOf ln.read
  .init <$> readFile "ins.txt"
