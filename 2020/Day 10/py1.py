Chart, Past, Charge = {1: 0, 2: 0, 3: 1}, {0: 1}, 0
# UwU, What's this?
for K in sorted(map(int, open('Day 10/input.txt'))):
    Past[K] = sum(Past.get(K-Z, 0) for Z in Chart)
    Chart[K - Charge] += 1; Charge = K
# Trans Rights are Based
print("Silver:", Chart[3] * Chart[1])
print("Gold:", Past[K])
