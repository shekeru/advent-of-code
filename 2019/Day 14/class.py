from collections import defaultdict; import re, math
# Python sucks
class Ext:
    def __init__(s, Yt, *Et):
        Fn = lambda x: (int(x[0]), x[1])
        s.Amnt, s.Name, *s.Products = *Fn(Yt), *map(Fn, Et)
        Graph[s.Name], s.Tick = s, 0
    def Synthesize(s, n = 0):
        for _, Pt in s.Products:
            if Pt in Graph:
                Graph[Pt].Synthesize(n + 1)
        Steps[s].add(n)
# Simulate Reactions
def Calculate(M = 1):
    local = defaultdict(int, {"FUEL": M})
    for J in sorted(Stage):
        for St in Stage[J]:
                cY = math.ceil(local[St.Name] / St.Amnt)
                for Ct, El in St.Products:
                    local[El] += Ct * cY
    return local["ORE"]
# Read Chemicals
Graph, Chem = {}, re.compile(r'(\d+)\s(\w+)')
with open("2019/Day 14/ins.txt") as Fr:
    [Ext(*Chem.findall(Ln)[::-1]) for Ln in Fr]
Steps, Stage = defaultdict(set), defaultdict(list)
# Place Reaction Stages
Graph["FUEL"].Synthesize()
for k, v in Steps.items():
    Stage[max(v)].append(k)
# Approximate Part 2's Reaction
Real = int(1e24 / Calculate(1e12))
while Calculate(Real) > 1e12:
    Real -= 1
# Fuck you again Eric Wastl
print("Silver:", Calculate())
print("Gold:", Real)
