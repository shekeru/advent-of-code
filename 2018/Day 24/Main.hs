module Main where

import Data.Function
import Input

main :: IO()
main = do
    xs <- Input.getFile
    print $ enemies xs (head xs)

enemies :: [Group] -> Group -> [Group]
enemies xs o = filter hostile xs
  where hostile = on (/=) _system o
