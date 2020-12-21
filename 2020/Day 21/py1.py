import re; from collections import *
Left, Right = defaultdict(int), defaultdict(int)
Relations = defaultdict(lambda: defaultdict(int))
Pr = re.compile("((?: ?\w+)+) \(contains((?: \w+,?)+)")
for Xs, Ys in Pr.findall(open("Day 21/input.txt").read()):
    for X in (Xs := Xs.split()):
        Left[X] += 1
    for Y in Ys.split(','):
        Y = Y.strip()
        Right[Y] += 1
        for X in Xs:
            Relations[X][Y] += 1
Part1, Part2 = 0, dict()
# Scrub Clean Ingredients
for X, Yds in Relations.copy().items():
    for Y in Yds.copy():
        if Right[Y] != Yds[Y]:
            del Yds[Y]
    if not len(Yds):
        Part1 += Left[X]
        del Relations[X]
# Resolve Ingredients -> Allergens
while (S := sorted(Relations, key = lambda X: len(Relations[X]))):
    V = Part2[(Y := [*Relations[V]][0])] = S.pop(0)
    for X in S:
        Relations[X].pop(Y, None)
    del Relations[V]
# Display Results
print("Silver:", Part1, "\nGold:", ",".
    join(Part2[X] for X in sorted(Part2)))
