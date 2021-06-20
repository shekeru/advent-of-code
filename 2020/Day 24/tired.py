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
# Functions
def Adjacent(*Coords):
    return (C := [Fn(*Coords) for Fn in Deltas.values()]), sum(World[Alt] for Alt in C)
def StepForwards(N):
    global World
    for _ in range(N):
        Next = collections.defaultdict(int)
        for Key, Value in (*World.items(),):
            # Remove the Whites
            if not Value:
                continue
            # Count the Blacks
            Nearby, Count = Adjacent(*Key)
            # Flip the Blacks
            if Count in (1, 2):
                Next[Key] = 1
            # Flip the Whites
            for Opt in Nearby:
                _, Count = Adjacent(*Opt)
                if Count == 2:
                    Next[Opt] = 1
        World = Next
    return sum(World.values())
# Init Tiles
for Current in Flips:
    Pt = 0, 0
    for I in Current:
        Pt = Deltas[I](*Pt)
    World[Pt] ^= 1
# Printing
print("Silver:", StepForwards(0))
print("Gold:", StepForwards(100))
