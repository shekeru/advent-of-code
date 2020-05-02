from collections import defaultdict; import math, re
# Read Chemicals
Chem = re.compile(r'(\d+)\s(\w+)')
with open("2019/Day 14/ins.txt") as f:
    Graph = {Pt: (Y, xs) for (Y, Pt), *xs
        in [[(int(N), el) for N, el in
    Chem.findall(ln)][::-1] for ln in f]}
# Check Tree for Balance
def Balanced(Tree):
    return all(Pt == "ORE" or
        Tree[Pt] <= 0 for Pt in Tree)
# Simulate Reactions
def Calculate(amnt):
    Local = defaultdict(int, {"FUEL": amnt})
    while not Balanced(Local):
        for Pt in Local.copy():
            if Pt != "ORE" and Local[Pt] > 0:
                Y, Table = Graph[Pt]
                cY = math.ceil(Local[Pt] / Y)
                for a, X in Table:
                    Local[X] += a * cY
                Local[Pt] -= cY*Y
    return Local["ORE"]
# Approximate Part 2's Reaction
Real = int(1e24 / Calculate(1e12))
while Calculate(Real) > 1e12:
    Real -= 1
# Fuck you again Eric Wastl
print("Silver:", Calculate(1))
print("Gold:", Real)
