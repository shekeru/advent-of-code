from heapq import *; import math
from collections import *
# Relative Positions
def Nearby(x, y):
    for j in (1, -1):
        yield x + j, y
        yield x, y + j
# Load Maze File
Map, Keys = {}, {}
with open('ins.txt') as F:
    for y, Ln in enumerate(F.read().splitlines()):
        for x, Ch in enumerate(Ln):
            if Ch != '#':
                if Ch.islower():
                    Keys[Ch] = y, x
                if Ch == '@':
                    for I, Crds in enumerate([(y+i, x+j) for j in (-1, 1)
                        for i in (-1, 1)], 1): Keys[str(I)] = Crds
                    Keys[Ch] = (Gold := (y, x))
                Map[y, x] = Ch
# World Class
class World:
    def __init__(s, Wh, Kh = '', Ln = 0):
        s.Where, s.Held, s.Steps = Wh, Kh, Ln
        s.Result = World.End == len(s.Held)
    End = len([x for x in Keys if x.islower()])
    def __hash__(s):
        return hash((*sorted(s.Held), s.Where))
    def __repr__(s):
        return repr((s.Where, s.Held, s.Steps))
    def __eq__(s, obj):
        return hash(s) == hash(obj)
    def __lt__(s, obj):
        return s.Steps < obj.Steps
    def GenerateBFS(s, Loc):
        Queue = deque([(0, *(Seen := {Keys[Loc]}), set())])
        while Queue:
            Ln, Tile, _Doors = Queue.popleft()
            for St in Nearby(*Tile):
                if all([St not in Seen, St in Map]):
                    if World.Mode and(St[0] == Gold[0]
                        or St[1] == Gold[1]): continue
                    Doors = _Doors.copy(); Seen.add(St)
                    if (Ch := Map[St]).isupper():
                        Doors.add(Ch.lower())
                    if Ch.islower(): World.Cache[Loc] \
                        .append((1 + Ln, Ch, Doors))
                    Queue.append((1 + Ln, St, Doors))
    def SearchCached(s):
        for Et in s.Where:
            if Et not in World.Cache:
                s.GenerateBFS(Et)
            for Ln, Ch, DrA in World.Cache[Et]:
                if not(Ch in s.Held or DrA - {*s.Held}):
                    yield World(s.Where.replace(Et, Ch),
                        s.Held + Ch, s.Steps + Ln)
    def Paths(Init): 
        World.Mode = len(Init) - 1
        World.Cache = defaultdict(list)
        Queue = list(Seen := {World(Init): 0})
        while Queue:
            if (Opt := heappop(Queue)).Result:
                return Opt.Steps
            for Sp in Opt.SearchCached():
                if Sp.Steps < Seen.get(Sp, math.inf):
                    Seen[Sp] = Sp.Steps; heappush(Queue, Sp)
# God this was awful
print('Silver:', World.Paths('@'))
print('Gold:', World.Paths('1234'))
