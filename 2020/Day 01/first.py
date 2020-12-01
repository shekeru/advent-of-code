from math import prod
from itertools import combinations
Xs = [int(x) for x in open('input.txt')]

def Solve(Rn):
    return prod({sum(Y): Y for Y in combinations(Xs, Rn)}[2020])

print("Silver:", Solve(2))
print("Gold:", Solve(3))
