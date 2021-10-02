import collections

Trans, World = {
    '^': lambda k: k + 1j,
    'v': lambda k: k - 1j,
    '>': lambda k: k + 1,
    '<': lambda k: k - 1,
}, collections.defaultdict(int,
    {0: int('111', 2)})

Workers = [
    lambda i, ch, v: Trans[ch](v),
    lambda i, ch, v: Trans[ch](v) if i % 2 else v,
    lambda i, ch, v: v if i % 2 else Trans[ch](v),
]; Ptrs, S, G = [0] * len(Workers), 0, 0

with open('2015/Day 03/input.txt') as F:
    Input = F.read().strip()

for I, Action in enumerate(Input):
    for K, Fn in enumerate(Workers):
        Ptrs[K] = Fn(I, Action, Ptrs[K])
        World[Ptrs[K]] |= 1 << K

for V in World.values():
    S += V & 1; G += bool(V & 2 | V & 4)

print(f"Silver: {S}\nGold: {G}")
