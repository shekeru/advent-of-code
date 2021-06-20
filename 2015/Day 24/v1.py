import itertools, operator, functools
# Sheky Input
Input = [*map(int, open('2015/Day 24/ins.txt'))]
# AoC 2015 Makes Me Sad
def Solve(Groups = 3):
    Ideal = sum(Input) // Groups
    for N in range(1, len(Input) - 1):
        if List := [functools.reduce(operator.mul, x, 1) for x in itertools
            .combinations(Input, N) if sum(x) == Ideal]: return min(List)
# Why is it so freaking simple
print("Silver:", Solve(), "\nGold:", Solve(4))
