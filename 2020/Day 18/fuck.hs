import Control.Monad
import Control.Monad.State
import Text.Printf

main = map (concat.words).lines <$> readFile "input.txt"
  >>= liftM2 (printf "Silver: %d\nGold: %d\n") silver gold

silver :: [String] -> Int
silver = sum.map (evalState expr) where
  expr = factor >>= loop where
    loop value = do
      tokens <- get
      if not (null tokens) && head tokens /= ')' then do
        let fn = case head tokens of '*' -> (*); '+' -> (+)
        put (tail tokens) >> factor >>= loop.fn value
      else pure value
  factor = do
    token <- get >>= liftM2 (>>) (put.tail) (pure.head)
    if token /= '(' then
      pure $read [token]
    else do
      value <- expr
      get >>= put.tail
      pure value

gold :: [String] -> Int
gold = sum.map (evalState expr) where
  expr = term >>= loop where
    loop value = do
      tokens <- get
      if not (null tokens) && head tokens == '*' then do
        put (tail tokens) >> term >>= loop.(*) value
      else pure value
  term = factor >>= loop where
    loop value = do
      tokens <- get
      if not (null tokens) && head tokens == '+' then do
        put (tail tokens) >> factor >>= loop.(+) value
      else pure value
  factor = do
    token <- get >>= liftM2 (>>) (put.tail) (pure.head)
    if token /= '(' then
      pure $read [token]
    else do
      value <- expr
      get >>= put.tail
      pure value
