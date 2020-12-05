def Bits(X):
    I = 0
    for x, c in enumerate(X[:7][::-1], 3):
        I |= int(c == 'B') << x
    for x, c in enumerate(X[7:][::-1]):
        I |= int(c == 'R') << x
    return I

F = {Bits(X.strip()) for X in open("input.txt")}
print("silver:", max(F), "\ngold:",
    max({*range(0, max(F))} - F))
