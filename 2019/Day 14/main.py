from collections import defaultdict; import math, re
# Read Chemicals
Chem = re.compile(r'(\d+)\s(\w+)')
with open("2019/Day 14/ins.txt") as f:
    Graph = {Pt: (Y, xs) for (Y, Pt), *xs
        in [[(int(N), el) for N, el in
    Chem.findall(ln)][::-1] for ln in f]}
Steps, Stage = defaultdict(set), defaultdict(list)
# Map Reaction Priority
def Synthesize(Pt, n = 0):
    for _, X in Graph[Pt][1]:
        if X in Graph:
            Synthesize(X, n+1)
    Steps[Pt].add(n)
# Simulate Reactions
def Calculate(M = 1):
    Material = defaultdict(int, {"FUEL": M})
    for J in sorted(Stage):
        for Pt in Stage[J]:
            Y, Table = Graph[Pt]
            cY = math.ceil(Material[Pt] / Y)
            for a, X in Table:
                Material[X] += a * cY
    return Material["ORE"]
# Place Reaction Stages
Synthesize("FUEL")
for k, v in Steps.items():
    Stage[max(v)].append(k)
# Approximate Part 2's Reaction
Real = int(1e24 / Calculate(1e12))
while Calculate(Real) > 1e12:
    Real -= 1
# Fuck you again Eric Wastl
print("Silver:", Calculate(1))
print("Gold:", Real)
