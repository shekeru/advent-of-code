import itertools, operator, functools
# AoC 2015 Makes Me Sad
def Solve(Groups = 3, Start = 2):
    Ideal = sum(Input) // Groups
    while sum(Input[:Start]) < Ideal:
        Start += 1
    for N in range(Start, len(Input) - Groups):
        if List := [functools.reduce(operator.mul, x, 1) for x in itertools
            .combinations(Input, N) if sum(x) == Ideal]: return min(List)
# Why is it so freaking simple
Input = sorted(map(int, open('2015/Day 24/ins.txt')), reverse
    = True); print("Silver:", Solve(), "\nGold:", Solve(4))
