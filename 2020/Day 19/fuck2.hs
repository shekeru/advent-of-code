{-# LANGUAGE ViewPatterns, BlockArguments #-}

import Text.Printf; import Data.Function
import Data.Functor; import Control.Monad
import qualified Data.Map.Strict as SM
import Data.List.Split

main :: IO ()
main = do
  (silver, strings) <- readF "input.txt"
  let generate rxs = foldr ((+).fromEnum.elem "".(mkTree rxs 0)) 0 strings
  on (printf "Silver: %d\nGold: %d\n") generate silver $foldr (\(k, v) ->
    SM.insert k $words v) silver [(8, "42 | 42 8"), (11, "42 31 | 42 11 31")]

mkTree :: Header -> Int -> Rule; type Rule = String -> [String]
mkTree graph ((SM.!) graph -> xs) | elem '"' (head xs) = basic
  | otherwise = (map (mkTree graph.read) <$> splitOn ["|"] xs >>=).foldM (&)
    where basic (c:str) | c == (head.read.head) xs = [str]; basic _ = []

readF :: String -> IO (Header, [String]); type Header = SM.Map Int [String]
readF wh = (\[hd, bd] -> (SM.fromList $map fn hd, bd)).splitOn [""].lines <$> readFile
  wh where fn (splitOn ":" -> ln) = let [idx, rule] = ln in (read idx, words rule)
