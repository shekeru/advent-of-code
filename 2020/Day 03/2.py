from math import prod
Map = open('input.txt').read().splitlines()
Slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def Solve(A, B):
    return [Map[Y][A * Y//B % 31] for Y
        in range(0, len(Map), B)].count('#')

print("Silver:", Solve(*Slopes[1]))
print("Gold:", prod([Solve(*v) for v in Slopes]))
