import collections

Positions, World = [[0], [0, 0]], \
    collections.defaultdict(int, {0: 1+2j})
Member, S, G = [0] * len(Positions), 0, 0

Trans = {
    '^': lambda k: k + 1j,
    'v': lambda k: k - 1j,
    '>': lambda k: k + 1,
    '<': lambda k: k - 1,
}

with open('2015/Day 03/input.txt') as F:
    Input = F.read().strip()

for Action in Input:
    for I, Level in enumerate(Positions):
        Level[Member[I]] = Trans[Action](Level[Member[I]])
        Member[I] = (Member[I] + 1) % len(Level)
        World[Level[Member[I]]] += 1j if I else 1

for V in World.values():
    S += 1 if V.real else 0
    G += 1 if V.imag else 0

print(f"Silver: {S}\nGold: {G}")
