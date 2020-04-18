from itertools import combinations
from collections import deque; import heapq
# Parsing Input
Starts, Graph, Map, Keys = {}, {}, {}, {}; where = 't3'
with open(f'{where}.txt') as F:
    for y, Ln in enumerate(F.read().split('\n')):
        for x, Ch in enumerate(Ln):
            if Ch != '#':
                if Ch.islower() or Ch == '@':
                    Keys[Ch] = y, x
                Map[y, x] = Ch
def Nearby(x, y):
    for a, b in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        yield x + a, y + b
# Firstpass BFS
Spaces, Visited = deque([(
    Keys['@'], '@', set()
)]), {Keys['@']: 0}
while Spaces:
    Node, Pr, oDoors = Spaces.popleft()
    for St in Nearby(*Node):
        Doors = oDoors.copy()
        if St in Visited or St not in Map:
            continue
        Visited[St] = Visited[Node] + 1
        if Map[St].islower():
            Ky, Dist = (*sorted([Pr, Map[St]]),), \
                Visited[St] - Visited[Keys[Pr]]
            if Pr == '@':
                Starts[Ky[1]] = Dist, Doors.copy()
            else:
                Graph[Ky] = Dist, Doors.copy()
            Doors.clear(); Pr = Map[St]
        elif Map[St].isupper():
            Doors.add(Map[St].lower())
        Spaces.append((St, Pr, Doors))
# Fill Implicit Edges
def I_BFS(An, Bn):
    Spaces = deque(Visited := {Keys[An]: 0})
    while Spaces:
        for St in Nearby(*(Node := Spaces.popleft())):
            if St in Visited or not(Ch := Map.get(St)):
                continue
            Visited[St] = Visited[Node] + 1
            if Ch == Bn:
                return Visited[St]
            Spaces.append(St)
for Opt in combinations(Starts, 2):
    key = (*sorted(Opt),); Graph[(*key,)] = I_BFS \
          (*key), Starts[Opt[0]][1] | Starts[Opt[1]][1]
# Graph Problem
Seen = {Opt: Ln for Opt, (Ln, Dt)
    in Starts.items() if not Dt}
Queue = [(Ln, Opt) for Opt, Ln in Seen.items()]
while Queue:
    _, NodeL = heapq.heappop(Queue)
    for Path in Graph:
        Ln, Doors = Graph[Path]; 
        if (Loc := NodeL[-1]) not in Path or Doors - {*NodeL}:
            continue
        Next = [Ch for Ch in Path if Ch != Loc][0]
        Seen[(NewL := NodeL + Next)] = Seen[NodeL] + Ln
        heapq.heappush(Queue, (Seen[NewL], NewL))
        if len({*NewL}) == len(Keys) - 1:
            print(NewL, Seen[NewL]); 5/0;
