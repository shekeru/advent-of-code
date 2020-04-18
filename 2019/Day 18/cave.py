from collections import deque
# Helper Functions
Keys, Doors = {}, {}
You, Valid = tuple(), set()
def Nearby(x, y):
    for a, b in Pairs:
        yield x + a, y + b
Pairs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
# Read Fucking Caves
with open('2019/Day 18/ta.txt') as f:
    for y, ln in enumerate(f.read().split('\n')):
        for x, c in enumerate(ln):
            if c == '#':
                continue
            if c.isupper():
                Doors[c] = y, x
                continue
            elif c.islower():
                Keys[c] = y, x
            elif c == "@":
                You = y, x
            Valid.add((y,x))
# Cunt Me
Keys
