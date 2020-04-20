from itertools import combinations
from collections import deque; import heapq
# Parsing Input
Starts, Graph, Map, Keys = {}, {}, {}, {}; where = 'ins'
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
Seen = set()
Queue = [(Ln, Opt, Opt) for Opt, (Ln, Dt)
    in Starts.items() if not Dt]
while Queue:
    Ln, Cur, Held = heapq.heappop(Queue)
    if len({*Held}) == len(Keys) - 1:
        print(Next + ':', Push[0], Push[2])
        Queue.clear(); break;
    for Path in Graph:
        Ln_A, Doors = Graph[Path]
        if Cur not in Path or Doors - {*Held}:
            continue
        Next = [Ch for Ch in Path if Ch != Cur][0]
        HeldL = Held if Next in Held else Held + Next
        if (Key := (Next, HeldL)) not in Seen:
            heapq.heappush(Queue, Push := (Ln + Ln_A, Next, HeldL))
            Seen.add(Key)
