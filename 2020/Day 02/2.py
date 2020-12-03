Silver = Gold = 0
for Ln in open("input.txt"):
    N, C, P = Ln.split(); C = C[0]
    A, B = map(int, N.split('-'))
    if A <= P.count(C) <= B:
        Silver += 1
    if [P[A-1], P[B-1]].count(C) == 1:
        Gold += 1

print("Silver:", Silver)
print("Gold:", Gold)
