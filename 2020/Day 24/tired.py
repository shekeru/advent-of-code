import re, collections
# Read File
Flips = tuple(map(re.compile(r'e|w|(?:s|n).')
    .findall, open('2020/Day 24/input.txt')))
# Used for Coords
Deltas, World = {
    'e': lambda x, y: (x - 1, y + 1),
    'w': lambda x, y: (x + 1, y - 1),
    'sw': lambda x, y: (x + 1, y),
    'ne': lambda x, y: (x - 1, y),
    'se': lambda x, y: (x, y + 1),
    'nw': lambda x, y: (x, y - 1),
}, collections.defaultdict(int)
# Part One
for Current in Flips:
    Pt = 0, 0
    for I in Current:
        Pt = Deltas[I](*Pt)
    World[Pt] ^= 1
# Display
print("Silver:", sum(1 for v
    in World.values() if v))
