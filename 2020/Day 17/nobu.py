import itertools, operator, functools
# Problem Functions
def Solve(V, N = 5):
    Next_To = [Opt for Pt in V for Opt in Nearby(Pt)]
    Births = filter(lambda Pt: 3 == Factor(Pt, V), Next_To)
    Deaths = filter(lambda Pt: Factor(Pt, V) not in (2, 3), V)
    V = V - {*Deaths} | {*Births}; return Solve(V, N - 1) if N else len(V)
def Nearby(Pt):
    return [(*map(operator.add, Pt, Crd),) for Crd in
        itertools.product([0, 1, -1], repeat = len(Pt))][1:]
def Factor(Pt, V):
    return functools.reduce(lambda s, k:
        s + int(k in V), Nearby(Pt), 0)    
# Read Input
World = {(X, Y, 0) for Y, Ln in enumerate \
    (open('input.txt').read().splitlines())
for X, t in enumerate(Ln) if t == '#'}
# Solve Problem
print("Silver:", Solve(World.copy()),
    "\nGold:", Solve({(*W, 0) for W in World}))
