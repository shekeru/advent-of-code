Array = []
for Ln in open("input.txt"):
    N, C, P = Ln.split(); C = C[:-1]
    N = (*map(int, N.split('-')),)
    Array.append((N, C, P))

Sum = 0
for (Min, Max), Ch, Pwd in Array:
    Rating = len([x for x in Pwd if x == Ch])
    if Min <= Rating and Rating <= Max:
        Sum += 1

print("Silver:", Sum)

Sum = 0
for Pos, Ch, Pwd in Array:
    Rating = sum([1 for I in Pos if Pwd[I-1] == Ch])
    if Rating == 1:
        Sum += 1

print("Gold:", Sum)
