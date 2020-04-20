from heapq import *; import math
from collections import *
# Parsing Input
Map, Keys = {}, {}; where = 'ins'
with open(f'{where}.txt') as F:
    for y, Ln in enumerate(F.read().splitlines()):
        for x, Ch in enumerate(Ln):
            if Ch != '#':
                if Ch.islower() or Ch == '@':
                    Keys[Ch] = y, x
                Map[y, x] = Ch
def Nearby(x, y):
    for j in (1, -1):
        yield x + j, y
        yield x, y + j
# World Class
class World:
    def Move(s, To, Add = 0):
        return World(To, s.Held + To, s.Steps + Add)
    Cache, End = defaultdict(list), len(Keys) - 1
    def __init__(s, Wh = '@', Kh = '', Ln = 0):
        s.Where, s.Held, s.Steps = Wh, Kh, Ln
        s.Result = World.End == len(s.Held)
    def __hash__(s):
        return hash((s.Where, *sorted(s.Held)))
    def __repr__(s):
        return repr((s.Where, s.Held, s.Steps))
    def __eq__(s, obj):
        return hash(s) == hash(obj)
    def __lt__(s, obj):
        return s.Steps < obj.Steps
    def GenerateBFS(s):
        Queue = deque([(0, *(Visited := {Keys[s.Where]}), set())])
        while Queue:
            Ln, Tile, _Doors = Queue.popleft()
            for St in Nearby(*Tile):
                if all([St not in Visited, St in Map]):
                    Doors = _Doors.copy(); Visited.add(St)
                    if (Ch := Map[St]).isupper():
                        Doors.add(Ch.lower())
                    if Ch.islower():
                        World.Cache[s.Where]. \
                            append((1 + Ln, Ch, Doors))
                    Queue.append((1 + Ln, St, Doors))
    def SearchCached(s):
        if s.Where not in World.Cache:
            s.GenerateBFS()
        for Ln, Ch, DrA in World.Cache[s.Where]:
            if not(Ch in s.Held or DrA - {*s.Held}):
                yield (Ch, Ln)
# This isn't even a graph anymore
Queue = list(Seen := {World(): 0})
while Queue:
    if (Opt := heappop(Queue)).Result:
        print('Silver:', Opt); break
    for Args in Opt.SearchCached():
        if (Sp := Opt.Move(*Args)).Steps < Seen.get(Sp, math.inf):
            Seen[Sp] = Sp.Steps; heappush(Queue, Sp)
