{-# LANGUAGE PartialTypeSignatures, ViewPatterns, FlexibleInstances, TupleSections, BlockArguments #-}

import Data.Function
import Control.Arrow
import Control.Monad
import qualified Data.Map.Strict as SM
import Data.List.Split
import Data.List

type Tile = (Int, [String])
type Edges = SM.Map Tile (Delta, Tile)
type Delta = (Pos -> Maybe Pos)
type TileMap = SM.Map Tile Pos
type Pos = (Int, Int)

instance Show Delta where
  show _ = "Delta_FN"

instance {-# OVERLAPS #-} Show Tile where
  show (i, xs) = show i

-- instance {-# OVERLAPS #-} Show [Tile] where
--   show xss = show $intercalate "\t" <$> transpose xss

-- instance {-# OVERLAPS #-} Show Tile where
--   show xs = intercalate "\n" $ "":xs <> [""]

t = readF "test-1.txt"

spin :: [String] -> [[String]]
spin xs = init$foldl fn [xs] [1..4] where
  fn ys@(transpose.head -> x) _ = (reverse x):x:ys

perms :: [Tile] -> Edges
perms xs = SM.fromList do
  [a, b] <- filter (\[a, b] -> on (/=) fst a b) $replicateM 2 xs
  case on check snd a b of
    Just dt -> pure (a, (dt, b))
    Nothing -> mempty

check :: [String] -> [String] -> Maybe Delta
check a b
  | (map head a) == (map last b) = Just \(x, y) ->
    if x > 0 then Just (x-1, y) else Nothing
  | head a == last b = Just \(x, y) ->
    if y > 0 then Just (x, y-1) else Nothing
  | otherwise = Nothing

readF :: String -> IO (Int, Edges)
readF wh = (floor.sqrt.fromIntegral.length &&& perms.concatMap fn).splitOn [""].lines <$>
  readFile wh where fn ((init.last.words -> idx):body) = (read idx,) <$> spin body

main :: IO ()
main = do
  (limit, edges) <- readF "input.txt"
  print $length edges
  print [g | g <- group $map fst $SM.keys edges]
  -- let yeet = map (\(a, b, c) -> b) edges
  -- print edges
  -- print $product [head g | g <- group $map fst yeet, length g == 8]
  -- print $map (\(a, b, c) -> (fst b, fst c)) edges
  -- print $length edges

-- lol :: [Edge] -> [_]
-- lol xs = map (length) do
--   alt <- permutations xs
--   let (_, yeet, _) = head alt
--   pure$ dfs (SM.singleton yeet (12, 12)) alt
--
-- dfs :: TileMap -> [Edge] -> TileMap
-- dfs v [] = v
-- dfs v (z@(dt, st, et):xs) = do
--   case SM.lookup st v of
--     Just pt -> do
--       let v' = case dt pt of
--             Just pt' -> SM.insert et pt' v
--             Nothing -> v
--       dfs v' xs
--     Nothing -> dfs v xs
