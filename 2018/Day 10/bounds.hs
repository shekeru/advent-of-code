{-#LANGUAGE QuasiQuotes#-}
import Text.RE.TDFA.String

main :: IO()
main = solve.map regex.lines <$> readFile "input.txt" >>= \(j, stars) -> do
  mapM_ putStrLn $format stars; putStrLn $"^- Spent "++show j++" Seconds -^"
  where regex = map read.matches.(*=~ [re|@{%int}|])

solve :: [[Int]] -> (Int, [(Int, Int)])
solve xss = head $dropWhile unbound [(i, [(x+u*i, y+v*i) | [x,y,u,v] <- xss]) | i <- [0..]]
  where unbound (_, xvs) = let (_, ys) = unzip xvs in maximum ys - minimum ys > 10

format :: [(Int, Int)] -> [String]
format xvs = [[if (x,y) `elem` xvs then '@' else ' ' | x <- range xs] | y <- range ys]
  where (xs, ys) = unzip xvs; range ys = [minimum ys .. maximum ys]
