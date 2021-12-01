with open('i1.txt') as fs:
    V = (*map(int, fs),)

def solve(t):
    return sum(int(J > I) for I, J in zip(V, V[t:]))

print("silver:", solve(1))
print("gold:", solve(3))
