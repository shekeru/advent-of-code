module Main where

main = do
  tree <- snd.mk_tree.map read.words <$> readFile "input.txt"
  putStrLn$ "Silver: " ++ (show $silver tree)
  putStrLn$ "Gold: " ++ (show $gold tree)

data Tree a = Node [Tree a] [a] deriving Show

mk_tree :: [Int] -> ([Int], Tree Int)
mk_tree (k:m:xs) = (drop m ys, Node (reverse ts) $take m ys)
  where (ys, ts) = foldr mk_nodes (xs, []) [1..k]

mk_nodes :: Int -> ([Int], [Tree Int]) -> ([Int], [Tree Int])
mk_nodes _ (xs,ts) = let (ys, t) = mk_tree xs in (ys, t:ts)

silver :: Tree Int -> Int
silver (Node ns vs) = sum vs + (sum $map silver ns)

gold :: Tree Int -> Int
gold (Node ns vs) = sum$ if null ns then vs else
  [gold.last$take v ns | v <- vs, v <= length ns]
