from itertools import combinations
from collections import deque; import heapq
# Parsing Input
Starts, Graph, Map, Keys = {}, {}, {}, {}; where = 't4'
with open(f'{where}.txt') as F:
    for y, Ln in enumerate(F.read().splitlines()):
        for x, Ch in enumerate(Ln):
            if Ch != '#':
                if Ch.islower():
                    Keys[Ch] = y, x
                if Ch == '@':
                    You = y, x
                Map[y, x] = Ch
def Nearby(x, y):
    for a, b in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        yield x + a, y + b
# Firstpass BFS
Seen = {(You, frozenset()): (0, '')}
Queue = deque(Seen)
while Queue:
    Pos, Set = Queue.popleft()
    Last, Ord = Seen[Pos, Set]
    for St in Nearby(*Pos):
        if St in Map and (St, Set) not in Seen:
            if Map[St].isupper() and Map[St].lower() not in Set:
                continue
            SetA = Set | {Map[St]} if Map[St].islower() else Set
            Queue.append(Next := (St, SetA)); Seen[Next] = \
                Last + 1, (Ord if SetA == Set else Ord + Map[St])
            if len(SetA) == len(Keys):
                print('Silver:', Seen[Next])
                Queue.clear(); break
