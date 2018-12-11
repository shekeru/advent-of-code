import math, itertools
def double_range(*xvs, t = 2):
    return [*itertools.product(range(*xvs), repeat = t)]
def reduction(x,y,i):
    return pts[i-1][(x,y)] + sum(pts[1][(x+u,y+v)] for
        (u,v) in {*double_range(i)} if (i-1) in (u,v))
def propagate_sums():
    for i in range(2, 5 or math.ceil(301**0.5)):
        pts[i] = {pair: reduction(*pair, i) for
            pair in double_range(1, 301 - i)}
def evaluate(grid,x,y):
    rID = x + 10; pLV = grid + rID * y
    return int(f"{pLV*rID:03d}"[-3]) - 5
pts = {1: {pair: evaluate(8141, *pair) for pair in double_range(1, 301)}}
_, sums = propagate_sums(), {j: max(pts[j].items(),
    key = lambda x: x[1]) for j in pts}; print(
'Silver: %s with %d' % sums[3]), print('Gold: %s with %d' %
    max(sums.items(), key = lambda x : x[1]))
sums[3]

# todo, fix formating
