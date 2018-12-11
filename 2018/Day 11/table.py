from collections import defaultdict
from itertools import product
def double_range(*xvs, t = 2):
    return [*product(range(*xvs), repeat = t)]
def evaluate(grid,x,y):
    rID = x + 10; pLV = grid + rID * y
    return int(f"{pLV*rID:03d}"[-3]) - 5
def adjust_cmp(value, u, v):
    return -value if u != v else value
def area_sum(x,y,i):
    return sum(adjust_cmp(pts[(x+u,y+v)], u, v)
        for (u,v) in product([0, i], repeat = 2))
def find_max(*boxes):
    return max({(x+1, y+1, j): area_sum(x, y, j) for j in boxes for
        (x,y) in double_range(301 - j)}.items(), key = lambda xs: xs[1])
pts = defaultdict(int)
for x, y in double_range(1, 301):
    pts[(x,y)] += evaluate(8141, x, y) - pts[(x-1, y-1)]
    pts[(x,y)] += pts[(x,y-1)] + pts[(x-1, y)]
print('Silver: %s with %d' % find_max(3))
print('Gold: %s with %d' % find_max(*range(1, 301)))
