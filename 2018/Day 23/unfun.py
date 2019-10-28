import re, math
with open('2018/Day 23/input.txt') as f:
    parse = lambda x: [*map(int, re.findall(r'-?\d+', x))]
    sys = [*map(parse, f.read().splitlines())]
st = max(sys, key = lambda pt: pt[3])
def m_dist(xs, ys):
    solve = lambda x, y: abs(y - x)
    return sum(solve(*pts) for pts in zip(xs[:3], ys[:3]))
amnt = [pts for pts in sys if m_dist(st, pts) <= st[3]]
# Fucking Part 2 Garbage
def solved():
    values, limit = set(), math.inf
    for ys in sys:
        dist = m_dist(3*[0], ys)
        if dist > ys[3]:
            values.add(dist - ys[3])
        limit = min(limit, dist + ys[3])
    return max(x for x in values if x < limit)
# Printing
print("Silver:", len(amnt))
print("Gold:", solved())

