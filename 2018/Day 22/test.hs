import Data.Foldable (foldl')
import Data.Map.Strict (Map, (!), insert, member, empty)
import Data.Set (Set, notMember)
import qualified Data.Set as S (insert, fromList)
import Data.Ix (range)
import qualified Data.PQueue.Min as Q
import Debug.Trace (traceShow)

type ErosionLevels = Map Coordinate Int
type Visiteds = Set Key
type Coordinate = (Int, Int) -- (x, y)
type Queue = Q.MinQueue (Int, Key)
type Key = (Coordinate, Tool)
data Tool = Torch | Climbing | Neither deriving (Eq, Ord, Show)

depth  = 3879
target = (8, 713) -- (x, y)
erosionMod = 20183

getErosionLevel :: (Int, ErosionLevels) -> Coordinate -> (Int, ErosionLevels)
getErosionLevel (_, els) coord@(x, y) =
    if   member coord els
    then (els ! coord, els)
    else calculated
    where calculated
            | coord == (0, 0) = (depth, insert coord depth els)
            | coord == target = (depth, insert coord depth els)
            | x == 0 =
                let val = (y * 48271 + depth) `mod` erosionMod
                in  (val, insert coord val els)
            | y == 0 =
                let val = (x * 16807 + depth) `mod` erosionMod
                in  (val, insert coord val els)
            | otherwise =
                let (up,   upEls)    = getErosionLevel (0, els)   (x, y - 1)
                    (left, rightEls) = getErosionLevel (0, upEls) (x - 1, y)
                    val = (up * left + depth) `mod` erosionMod
                in  (val, insert coord val rightEls)

getRiskLevel :: ErosionLevels -> Coordinate -> (Int, ErosionLevels)
getRiskLevel els coord =
    let (val, els') = getErosionLevel (0, els) coord
    in  (val `mod` 3, els')

-- getBinding :: erosion levels -> source binding -> target coordinate -> (target binding, updated erosion levels)
getBinding :: ErosionLevels -> (Int, Key) -> Coordinate -> ((Int, Key), ErosionLevels)
getBinding els ((sTime, (sCoord, sTool))) tCoord =
    let (sType, sEls) = getRiskLevel els  sCoord
        (tType, tEls) = getRiskLevel sEls tCoord
        (time, tool)  = getTimeTool sType tType (sTime, sTool)
    in  (if tCoord == target && tool /= Torch then (time + 7, (tCoord, Torch)) else (time, (tCoord, tool)), tEls)
    where
        getTimeTool :: Int -> Int -> (Int, Tool) -> (Int, Tool)
        getTimeTool 0 2 (time, Climbing) = (time + 8, Torch)       -- rocky  -> narrow
        getTimeTool 1 2 (time, Climbing) = (time + 8, Neither)     -- wet    -> narrow
        getTimeTool 0 1 (time, Torch)    = (time + 8, Climbing)    -- rocky  -> wet
        getTimeTool 2 1 (time, Torch)    = (time + 8, Neither)     -- narrow -> wet
        getTimeTool 1 0 (time, Neither)  = (time + 8, Climbing)    -- wet    -> rocky
        getTimeTool 2 0 (time, Neither)  = (time + 8, Torch)       -- narrow -> rocky
        getTimeTool _ _ (time, tool)     = (time + 1, tool)

getTargetTime :: Visiteds -> (Queue, ErosionLevels) -> Int
getTargetTime vis (q, els) =
    let Just (region@((time, (coord, t))), q') = Q.minView q
        neighbours = getNeighbours coord
    in  if   coord == target then time
        else if notMember (coord,t) (traceShow (length vis) vis)
               then getTargetTime (S.insert (coord,t) vis) $ foldl' (insertCoord region) (q', els) neighbours
               else getTargetTime vis (q', els)
    where
        -- source binding -> (queue, erosion levels) -> target coordinate -> (queue with target binding, updated erosion levels)
        insertCoord :: (Int, Key) -> (Queue, ErosionLevels) -> Coordinate -> (Queue, ErosionLevels)
        insertCoord region (q, els) coord =
            let (binding, els') = getBinding els region coord
            in  (Q.insert binding q, els')
        getNeighbours :: (Int, Int) -> [(Int, Int)]
        getNeighbours coord@(x, y) = filter (\coord@(x, y) -> x >= 0 && y >= 0)
            [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]

part1 :: Int
part1 = sum . fmap (`mod` 3) . snd . foldl' getErosionLevel (0, empty) $ range ((0, 0), target)

part2 :: Int
part2 =
    let q = Q.fromList $ [(0,((0, 0), Torch))]
        vis = S.fromList []
    in  getTargetTime vis (q, empty)

main :: IO ()
main = do
    print part1
    print part2
