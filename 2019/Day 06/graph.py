with open("2019/Day 06/input.txt") as f:
    V, Graph = 0, {}
    for LN in f.readlines():
        Pr, Ch = LN.strip().split(')')
        Graph[Ch] = Pr
        
def Flatten(N):
    while N in Graph:
        N = Graph[N]
        yield N

SN = [*Flatten('SAN')]
for N in Graph:
    while N in Graph:
        N = Graph[N]
        V += 1

for I, N in enumerate(Flatten('YOU')):
    if N in SN:
        break

print("Silver:", V)
print("Gold:", SN.index(N) + I)
