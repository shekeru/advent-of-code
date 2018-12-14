module Main where

import Data.Digits

type State = ([Int], Int, Int)

main = do
  let const = 30121
  let (numbers, u, v) = sets!!(const+10)
  print$ take 20 $drop (const-10) $reverse numbers
  --mapM_ print (reverse numbers)

sets :: [State]
sets = iterate next ([7,3], 0, 1)

next :: State -> State
next (xs, u, v) = (xs', f' u, f' v) where
  xs' = foldl (flip (:)) xs$ if null ys then [0] else ys
  f' j = mod (j + 1 + ret j) $length xs'
  ret i = xs !! (length xs - 1 - i)
  ys = digits 10 (ret u + ret v)
