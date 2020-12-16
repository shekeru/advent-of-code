from collections import Counter
from itertools import groupby
from functools import reduce
from math import prod
# UwU, What's this?
At = [0, *sorted(map(int, open('Day 10/input.txt')))]
At += [At[-1] + 3]; V = [y-x for x, y in zip(At, At[1:])]
# Suck It Incels
def Unique(V):
    return int(not V) if V <= 0 else \
        sum(Unique(V-o) for o in range(1, 4))
# Trans Rights are Based
print("Silver:", prod(Counter(V).values()))
print("Gold:", prod(Unique(len([*y]))
    for x, y in groupby(V) if x < 3))
