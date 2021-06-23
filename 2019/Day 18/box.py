from collections import *
import queue, math
# Helpers
class Path:
    def __init__(s, Wh, Kh, Ln = 0):
        s.Where, s.Keys, s.Steps = Wh, Kh, Ln
    def __repr__(s):
        return repr((s.Where, s.Steps, "".join(s.Keys)))
    def __hash__(s):
        return hash((*sorted(s.Keys), s.Where))
    def __eq__(s, o):
        return hash(s) == hash(o)
    def __lt__(s, o):
        return s.Steps < o.Steps

def Nearby(x, y):
    for j in (1, -1):
        yield x + j, y
        yield x, y + j
# Functions
def MkGraph(From, Mode = False):
    Stack = deque([(1, *(Seen := {Keys[From]}), set())])
    while Stack:
        Ln, Ptr, _Doors = Stack.popleft()
        for Opt in Nearby(*Ptr):
            if Opt in Map and Opt not in Seen:
                if Mode and Opt in Nearby(*Keys['@']):
                    continue
                Doors = _Doors.copy(); Seen.add(Opt)
                if (Ch := Map[Opt]).isupper():
                    Doors.add(Ch.lower())
                elif Ch.islower():
                    Graph[From].append((Ln, Ch, Doors))
                    if Ch not in Graph:
                        MkGraph(Ch, Mode)
                    continue
                Stack.append((Ln + 1, Opt, Doors))

def Search(From):
    Queue = queue.PriorityQueue()
    Queue.put(*(Seen := {Path(From, set()): 0}))
    while not Queue.empty():
        if len((Current := Queue.get()).Keys) == Total:
            return Current
        for Et in Current.Where:
            for Ln, Ch, Reqs in Graph[Et]:
                if not Reqs - Current.Keys:
                    NewPath = Path(Current.Where.replace(Et, Ch),
                        Current.Keys | {Ch}, Current.Steps + Ln)
                    if NewPath.Steps < Seen.get(NewPath, math.inf):
                        Queue.put(NewPath); Seen[NewPath] = NewPath.Steps
# Parsing
Map, Keys = {}, {}
with open('ins.txt') as F:
    for Y, Ln in enumerate(F.read().split()):
        for X, Ch in enumerate(Ln):
            if Ch != "#":
                if not Ch.isupper():
                    Keys[Ch] = Y, X
                if Ch == '@':
                    for I, Crds in enumerate([(Y+i, X+j) for j in (-1, 1)
                        for i in (-1, 1)], 1): Keys[str(I)] = Crds
                Map[Y, X] = Ch
Total = sum(1 for x in Keys if x.islower())
# Printing
Graph = defaultdict(list); MkGraph('@')
print("silver:", Search('@').Steps)
Graph = defaultdict(list)
[MkGraph(x, True) for x in '1234']
print("gold:", Search('1234').Steps)
