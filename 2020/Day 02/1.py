Array = []
for Ln in open("input.txt"):
    N, C, P = Ln.split(); C = C[0]
    N = (*map(int, N.split('-')),)
    Array.append((N, C, P))

print("Silver:", sum([1 for (Min, Max), Ch, Pwd
    in Array if Min <= Pwd.count(Ch) <= Max]))

print("Gold:", sum([1 for Pos, Ch, Pwd in Array if
    sum([1 for I in Pos if Pwd[I-1] == Ch]) == 1]))
