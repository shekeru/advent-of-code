from collections import Counter
from itertools import groupby
from functools import reduce
from math import prod
# UwU, What's this?
At = [0, *sorted(map(int, open('Day 10/input.txt')))]
At += [At[-1] + 3]; V = [y-x for x, y in zip(At, At[1:])]
# Suck It Incels
def Unique(V):
    if V not in At or V <= 0:
        return int(not V)
    return sum(Unique(V-o) for o in range(1, 4))
# Trans Rights are Based
print("Silver:", prod(Counter(V).values()))
print("Gold:", prod(Unique(len([*y]))
    for x, y in groupby(V) if x < 3))
