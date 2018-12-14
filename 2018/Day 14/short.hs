module Main where

import Data.Digits

type State = ([Int], Int, Int)

main = do
  let const = 30121
  let (numbers, u, v) = sets!!(const+10)
  --print$ take 20 $drop (const-10) $reverse numbers
  mapM_ print (reverse numbers)

sets :: [State]
sets = iterate next ([7,3], 0, 1)

next :: State -> State
next (xs, u, v) = (xs', f' u, f' v) where
  f' j = mod (length xs' - j - 1 + length ys - xs!!j) $length xs'
  xs' = foldl (flip (:)) xs$ if null ys then [0] else ys
  ys = digits 10 (xs!!u + xs!!v)
