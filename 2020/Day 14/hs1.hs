{-# LANGUAGE ViewPatterns, TupleSections #-}
import qualified Data.Map.Strict as SM
import Data.Bits (setBit, clearBit)
import Control.Monad (liftM2, ap)
import Text.Printf (printf)
import Data.Function (on)

type Mask = [(Int, Char)]
type Section = (Mask, [Write])
type Write = (Int, Int)

main :: IO ()
main = do
  series <- fmap (sum.SM.elems.SM.fromList).(>>=).reverse <$> input
  on (printf "Silver: %d\nGold: %d\n") series silver gold

silver :: Section -> [Write]
silver (mask, xs) = foldl fn [] xs where
  fn ys (key, val) = (key, foldr bits val mask): ys
  bits (i, '0') = (`clearBit` i)
  bits (i, '1') = (`setBit` i)
  bits _ = id

gold :: Section -> [Write]
gold (mask, xs) = foldl fn [] xs where
  fn ys (key, val) = map (,val) (foldr bits [key] mask) <> ys
  bits (i, 'X') = ap [(`setBit` i), (`clearBit` i)]
  bits (i, '1') = fmap (`setBit` i); bits _ = id

input :: IO [Section]
input = foldl parse mempty.lines <$> readFile "input.txt" where
  parse acc (words -> ln)
    | head ln == "mask" = (zip [35, 34..] $last ln, []): acc
    | otherwise = (mask, next:writes): tail acc where
      next = liftM2 (on (,) read) (init.drop 4.head) last ln
      (mask, writes) = head acc
