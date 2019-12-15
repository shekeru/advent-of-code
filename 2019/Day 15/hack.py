from dataclasses import dataclass
from collections import deque
# Helper Functions
def Nearby(x, y):
    for a, b in Pairs:
        yield x + a, y + b
Pairs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
# Read Intcode Tape
with open('2019/Day 15/ins.txt') as f:
    Tape = [*map(int, f.read().split(','))]
Converter = (Tape[146], Tape[153])
# Reversed Class
@dataclass
class Position:
    x: int = 0; y: int = 0
    a: int = 0; b: int = 0
    def Update(s, x, y):
        s.x, s.y = x, y
        s.a = s.x & 1
        s.b = s.y & 1
        return s.Block()
    def Index(s):
        v = s.y // 2
        v += s.b - 1
        v *= 39
        v += s.x - 1
        return Tape[v + 252]
    def Block(s):
        if 0 in (s.x, s.y) or 40 in (s.x, s.y):
            return 0
        if (s.x, s.y) == Converter:
            return 2
        if s.x == 21 and s.y == 21:
            return 3
        if not (s.a | s.b):
            return 0
        if (s.a & s.b):
            return 1
        return int(s.Index() < Tape[212])
# It Really Doesn't Matter
Visited, Pt = {Converter: 0}, Position()
Start, Spaces = (21, 21), deque(Visited)
while Spaces:
    Node = Spaces.popleft()
    if not Pt.Update(*Node):
        continue
    for Y in Nearby(*Node):
        if Y not in Visited:
            Visited[Y] = Visited[Node] + 1
            if Pt.Update(*Y) == 1:
                Spaces.append(Y)
# Fuck you Eric Wastl
print("Silver:", Visited[Start])
print("Gold:", max(Visited.values()))
# Maze Printing
chars = ["█", " ","@", "x"]
print("\n".join("".join(
    chars[Pt.Update(x, y)] for x in
range(0, 41)) for y in range(0, 41)))
