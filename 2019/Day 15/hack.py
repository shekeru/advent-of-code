from dataclasses import dataclass
with open('2019/Day 15/terry.txt') as f:
    Tape = [*map(int, f.read().split(','))]
# Reversed Class
@dataclass
class Position:
    x: int = 0
    y: int = 0
    a: int = 0
    h: int = 0
    b: int = 0
    def update(s, x, y):
        s.x, s.y = x, y
        s.h = s.y // 2
        s.a = s.x & 1
        s.b = s.y & 1
        return s.block()
    def Index(s):
        v = s.h + s.b
        v = (v - 1) * 39
        v += s.x - 1
        return Tape[v + 252]
    def block(s):
        if 0 in (s.x, s.y) or 40 in (s.x, s.y):
            return 0
        if s.x == Tape[146] and s.y == Tape[153]:
            return 2
        if s.x == 21 and s.y == 21:
            return 3
        if not (s.a | s.b):
            return 0
        if (s.a & s.b):
            return 1
        return int(s.Index() < Tape[212])
Pt = Position()
# Printing
char = ["█", " ","@", "x"]
for y in range(0, 41):
    print(*(char[Pt.update(x, y)] for
        x in range(0, 41)), sep = "")
