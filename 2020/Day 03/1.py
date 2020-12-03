Map, Slopes = {(x, y): int(Ch == '#') for (y, Ln) in
    enumerate(open('input.txt')) for (x, Ch) in enumerate(Ln)
if Ch != '\n'}, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
Mx, My = max(Map.keys()); from math import prod

def Solve(A, B):
    S = X = Y = 0
    while Y <= My:
        S += Map[X, Y]
        X, Y = (X + A) % \
            (Mx + 1), Y + B
    return S

print("Silver:", Solve(*Slopes[1]))
print("Gold:", prod([Solve(*v) for v in Slopes]))
