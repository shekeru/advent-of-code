{-#LANGUAGE QuasiQuotes#-}
import Control.Applicative
import Text.RE.TDFA.String
import Data.List.Split
import Text.Printf
import Data.List

main :: IO ()
main = filter ((== 7).length.intersect keys.map head)
  <$> input >>= liftA2 (>>) (printf "Silver: %d\n".length)
    (printf "Gold: %d\n".length.filter (all verify)) where
      keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

verify :: [String] -> Bool
verify ["byr", v] = matched $v ?=~ [re|^(19[2-9][0-9]|200[0-2])$|]
verify ["iyr", v] = matched $v ?=~ [re|^(201[0-9]|2020)$|]
verify ["eyr", v] = matched $v ?=~ [re|^(202[0-9]|2030)$|]
verify ["hgt", v] = matched $v ?=~ [re|^((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$|]
verify ["hcl", v] = matched $v ?=~ [re|^#[0-9a-f]{6}$|]
verify ["ecl", v] = matched $v ?=~ [re|^(amb|blu|brn|gry|grn|hzl|oth)$|]
verify ["pid", v] = matched $v ?=~ [re|^[0-9]{9}$|]
verify ["cid", _] = True

input :: IO [[[String]]]
input = map(map (splitOn ":").words)
  .splitOn "\n\n" <$> readFile "input.txt"
