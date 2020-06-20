import collections
# Functions
def Search(Y, X):
    Horizontal = (Y, X-1), (Y, X), (Y, X+1)
    yield Horizontal; yield Horizontal[::-1]
    Vertical = (Y-1, X), (Y, X), (Y+1, X)
    yield Vertical; yield Vertical[::-1]
def Nearby(x, y):
    for j in (1, -1):
        yield x + j, y
        yield x, y + j
# Read to Map
Map, List = {}, {}
with open("input.txt") as Fr:
    for Y, Ln in enumerate(Fr, 1):
        for X, Ch in enumerate(Ln, 1):
            if Ch not in "# \n":
                Map[Y,X] = Ch
# Gated Structure
for Key, Ch in [*Map.items()]:
    if Ch.isupper():
        for Crds in Search(*Key):
            V = [*filter(None, map(Map.get, Crds))]
            if len(V) == 3 and V[0] == '.':
                A, B, C = Crds; del Map[B]
                Name = "".join(sorted(V[1:]))
                if Name in List:
                    B1, A1 = List[Name]
                    Map[B], Map[B1] = A1, A
                else:
                    List[Name] = [B, A]
                if Name == 'AA':
                    Start = A
                if Name == 'ZZ':
                    End = A
                del Map[C]
# BFS Time
Queue = collections.deque(Seen := {Start: 0})
while Queue:
    Step = Queue.popleft()
    for St in Nearby(*Step):
        if St in Map and St not in Seen:
            if not isinstance(Map[St], str):
                St = Map[St]
            Seen[St] = Seen[Step] + 1
            Queue.append(St)
    if Step == End:
        print("Silver:", Seen[Step])
        break
# Scan Edges
for (A, B), Ch in Map.items():
    if not isinstance(Ch, str):
        Map[A, B] = Ch, -1 if 2 in (A, B) \
            or A == Y -1 or B == X -2 else 1
# Re-BFS
"fuck"
