module Main where

import Text.Printf
import Crypto.Hash.MD5 (hash)
import Data.ByteString.Base16 (encode)
import Data.ByteString.Char8 (pack, unpack)

main :: IO ()
main = do
  printf "Silver: %d\n" $ search 5 1
  printf "Gold: %d\n" $ search 6 1

search :: Int -> Int -> Int
search n x = let md5 = digest x in if
  n > length (takeWhile (== '0') md5)
    then search n (x + 1) else x

digest :: Int -> String
digest = unpack.encode.hash
  .pack.(++) secret.show

secret :: String
secret = "ckczppom"
