{-#LANGUAGE QuasiQuotes#-}
import Control.Applicative
import Text.RE.TDFA.String
import Data.List.Split
import Control.Arrow
import Text.Printf
import Data.List
import Data.Char

main :: IO ()
main = filter ((== 7).length.intersect keys.map head)
  <$> input >>= liftA2 (>>) (printf "Silver: %d\n".length)
    (printf "Gold: %d\n".length.filter (all verify)) where
      keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

verify :: [String] -> Bool
verify ["byr", v] = liftA2 (&&) (1920 <=) (<= 2002) $read v
verify ["iyr", v] = liftA2 (&&) (2010 <=) (<= 2020) $read v
verify ["eyr", v] = liftA2 (&&) (2020 <=) (<= 2030) $read v
verify ["hgt", v] = maybe False (fn <<< dropWhile isDigit &&& read.
  takeWhile isDigit) $matchedText $v ?=~ [re|^@{%int}(cm|in)$|] where
    fn ("cm", x) = liftA2 (&&) (150 <=) (<= 193) x
    fn ("in", x) = liftA2 (&&) (59 <=) (<= 76) x
verify ["hcl", v] = matched $v ?=~ [re|^#[0-9a-f]{6}$|]
verify ["ecl", v] = matched $v ?=~ [re|^(amb|blu|brn|gry|grn|hzl|oth)$|]
verify ["pid", v] = matched $v ?=~ [re|^[0-9]{9}$|]
verify ["cid", _] = True

input :: IO [[[String]]]
input = map(map (splitOn ":").words)
  .splitOn "\n\n" <$> readFile "input.txt"
