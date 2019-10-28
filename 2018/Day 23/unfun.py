import re
with open('2018/Day 23/input.txt') as f:
    parse = lambda x: [*map(int, re.findall(r'-?\d+', x))]
    sys = [*map(parse, f.read().splitlines())]
st = max(sys, key = lambda pt: pt[3])
def m_dist(xs, ys):
    solve = lambda x, y: abs(y - x)
    return sum(solve(*pts) for pts in zip(xs[:3], ys[:3]))
# Fucking Part 2 Garbage
def flatten(sys):
    for ys in sys:
        dist = m_dist((0, 0, 0), ys)
        if dist > ys[3]:
            yield (dist - ys[3], True)
            yield (dist + ys[3], False)
def solved():
    for value, ok in sorted(flatten(sys)):
        if not ok:
            break
        yield value
# Printing
print("Silver:", len([pts for pts in sys if
    m_dist(st, pts) <= st[3]]))
print("Gold:", 
    [*solved()][-1])
