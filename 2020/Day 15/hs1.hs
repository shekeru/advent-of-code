import qualified Data.IntMap.Strict as SM
import Control.Monad.ST
import Control.Monad
import Text.Printf
import Data.STRef

main :: IO ()
main = do
  let (offset, input) = length >>= (,) $[1,2,16,19,18,0]
  let fn = turn (SM.fromList $ zip input [1..]) offset
  printf "Silver: %d\nGold: %d\n" (fn 2020) (fn 30000000)

turn :: SM.IntMap Int -> Int -> Int -> Int
turn v0 t nth = runST $do
  vref <- newSTRef v0
  (\f -> foldM f 0 [t+1..nth-1])$ \c t -> do
    v <- readSTRef vref
    modifySTRef' vref (SM.insert c t)
    pure $t - SM.findWithDefault t c v
