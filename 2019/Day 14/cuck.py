from collections import defaultdict; import math, re
# Fucking Hell Today
Chem = re.compile(r'((\d+)\s(\w+))')
# Read Chemicals
with open("2019/Day 14/ins.txt") as f:
    Graph = {Pt: (Y, xs) for (Y, Pt), *xs in [[
        (int(N), el) for N, el in (Rt[1:] for Rt in
    Chem.findall(ln))][::-1] for ln in f.readlines()]}
Order, Stage = defaultdict(set), defaultdict(set)
# Map Reaction Priority
def Synthesize(Pt, n = 0):
    if Pt not in Graph:
        return
    Order[Pt].add(n)
    for _, X in Graph[Pt][1]:
        Synthesize(X, n+1)
# Reduce Element
def React(N, Pt):
    Y, table = Graph[Pt]
    Rl = math.ceil(N/Y)
    for a, el in table:
        yield a * Rl, el
# Simulate Reactions
def Calculate(M = 1):
    Elements = defaultdict(int, [("FUEL", M)])
    for J in sorted(Stage):
        for Pt in Stage[J]:
            for N, X in React(Elements[Pt], Pt):
                Elements[X] += N
            del Elements[Pt]
    return Elements["ORE"]
# Fix Reaction Stages
Synthesize("FUEL")
for k, v in Order.items():
    Stage[max(v)].add(k)
# Estimate Solution
Real = int(1e24 / Calculate(1e12))
# Error Correction
while Calculate(Real) > 1e12:
    Real -= 1
# Fuck you Eric
print("Silver:", Calculate(1))
print("Gold:", Real)
