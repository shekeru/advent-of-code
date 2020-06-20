from collections import deque
# Helper Functions
def Nearby(x, y):
    for j in (1, -1):
        yield x + j, y
        yield x, y + j
# Reversed Function
def Render(x, y):
    a, b = x & 1, y & 1
    if 0 in (x, y) or 40 in (x, y):
        return 0
    if (x, y) == Converter:
        return 2
    if (x, y) == Start:
        return 3
    if not (a | b):
        return 0
    if (a & b):
        return 1
    return int(Tape[39 *(b +y //2 -1) +x +251] < Tape[212])
# Read Intcode Tape
with open('ins.txt') as f:
    Tape = [*map(int, f.read().split(','))]
Start, Converter = (21, 21), (Tape[146], Tape[153])
Spaces = deque(Visited := {Converter: 0})
# Search Spaces
while Spaces:
    Node = Spaces.popleft()
    for St in Nearby(*Node):
        if St not in Visited and Render(*St):
            Visited[St] = Visited[Node] + 1
            Spaces.append(St)
# Fuck you Eric Wastl
print("Silver:", Visited[Start])
print("Gold:", max(Visited.values()))
# Maze Printing
chars = ["█", " ","@", "x"]
print("\n".join("".join(
    chars[Render(x, y)] for x in
range(0, 41)) for y in range(0, 41)))
