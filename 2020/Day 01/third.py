def silver():
    for I in range(N - 1):
        for J in range(I + 1, N):
            if Xs[I] + Xs[J] == 2020:
                return Xs[I] * Xs[J]

def gold():
    for I in range(N - 2):
        A, s, e = Xs[I], I + 1, N - 1
        while s < e:
            B, C = Xs[s], Xs[e]
            if A + B + C == 2020:
                return A * B * C
            elif A + B + C > 2020:
                e -= 1; continue
            s += 1
            
Xs = [*sorted(int(x) for x in open('input.txt'))]
N = len(Xs)
print("silver:", silver())
print("gold:", gold())
