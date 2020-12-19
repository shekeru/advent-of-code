import Data.Char (isDigit)

main :: IO ()
main = do
  maths <- sequence.map (flip solve.concat.words).lines <$> readFile
    "input.txt"; mapM_ (print.sum.maths) [const 0, fromEnum.('+' ==)]

solve :: (Char -> Int) -> String -> Int
solve prec = go [] [].reverse where
  place ch ops = prec ch >= prec (head $ops <> [ch])
  go acc ops (')':ts) = go acc (')':ops) ts
  go acc (')':ops) ('(':ts) = go acc ops ts
  go acc ops ('*':ts) | place '*' ops = go acc ('*':ops) ts
  go acc ops ('+':ts) | place '+' ops = go acc ('+':ops) ts
  go acc ops (ch:ts) | isDigit ch = go (read [ch]:acc) ops ts
  go (x:y:acc) ('*':ops) ts = go (x * y:acc) ops ts
  go (x:y:acc) ('+':ops) ts = go (x + y:acc) ops ts
  go [res] [] [] = res
