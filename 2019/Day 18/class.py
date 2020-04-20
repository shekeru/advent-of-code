from collections import deque; from heapq import *
from itertools import combinations; import math
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
    for a, b in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        yield x + a, y + b
# World Class
class World:
    @property
    def Position(s):
        return Keys[s.Where]
    # Built Ins
    def __init__(s, Wh = '@', Kh = '', Ln = 0):
        s.Where, s.Held, s.Steps = Wh, Kh, Ln
    def __hash__(s):
        return hash((s.Where, *sorted(s.Held)))
    def __repr__(s):
        return repr((s.Where, s.Held, s.Steps))
    def __eq__(s, obj):
        if isinstance(obj, World):
            return hash(s) == hash(obj)
    def __lt__(s, obj):
        return s.Steps < obj.Steps
    # Search Functions
    def Move(s, To, Add = 0):
        return World(To, s.Held + To, s.Steps + Add)
    def Search(s):
        global i
        Queue = deque(Visited := {s.Position: 0})
        while Queue:
            Tile = Queue.popleft()
            for St in Nearby(*Tile):
                if all([St not in Visited, St in Map]):
                    if (Ch := Map[St]).isupper() and Ch.lower() not in s.Held:
                        continue
                    Visited[St] = Visited[Tile] + 1
                    if Ch.islower() and Ch not in s.Held:
                        yield (Ch, Visited[St])
                    else:
                        Queue.append(St)
            i += 1
# This isn't even a graph anymore
Queue = [*(Seen := {World(): 0})]
i = 0
while Queue:
    Opt = heappop(Queue)
    if len(Opt.Held) == len(Keys) - 1:
        print(Opt); break;
    for Args in Opt.Search():
        if (Sp := Opt.Move(*Args)).Steps < Seen.get(Sp, math.inf):
            Seen.pop(Sp, 1); Seen[Sp] = Sp.Steps; heappush(Queue, Sp)
print(i)
