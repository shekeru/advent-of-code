import re, math
with open('2018/Day 25/input.txt') as f:
    parse = lambda x: [*map(int, re.findall(r'-?\d+', x))]
    sys = [*map(parse, f.read().splitlines())]
def m_dist(xs, ys):
    solve = lambda x, y: abs(y - x)
    return sum(solve(*pts) for pts in zip(xs, ys))
const, was = 0, False
for i in range(len(sys) - 1):
    if m_dist(sys[i], sys[i+1]) <= 3:
        was = True; continue
    if was:
        const += 1
    was = False
print("Silver:", const)
