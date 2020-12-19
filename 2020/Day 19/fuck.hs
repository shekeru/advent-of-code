{-# LANGUAGE ViewPatterns, BlockArguments #-}

import Text.Printf; import Data.Function
import qualified Data.Map.Strict as SM
import Data.List.Split

main :: IO ()
main = do
  (silver, strings) <- readF "input.txt"
  let generate rxs = foldr ((+).fromEnum.elem "".eval (mkTree rxs 0)) 0 strings
  on (printf "Silver: %d\nGold: %d\n") generate silver $foldr (\(k, v) ->
    SM.insert k $words v) silver [(8, "42 | 42 8"), (11, "42 31 | 42 11 31")]
data Rule = Basic (String -> [String]) | Complex [[Rule]]

eval :: Rule -> String -> [String]
eval (Complex rss) xs = rss >>=
  foldl ((.eval).(>>=)) [xs]
eval (Basic ch) xs = ch xs

mkTree :: Header -> Int -> Rule
mkTree graph ((SM.!) graph -> xs) | elem '"' (head xs) = Basic fn
  | otherwise = Complex $map (map $mkTree graph.read) $splitOn ["|"] xs
    where fn (c:str) | c == (head.read.head) xs = [str]; fn _ = []

readF :: String -> IO (Header, [String]); type Header = SM.Map Int [String]
readF wh = (\[hd, bd] -> (SM.fromList $map fn hd, bd)).splitOn [""].lines <$> readFile
  wh where fn (splitOn ":" -> ln) = let [idx, rule] = ln in (read idx, words rule)
