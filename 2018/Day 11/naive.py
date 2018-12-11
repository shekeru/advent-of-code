from itertools import product
def double_range(*xvs):
    return [*product(range(*xvs), repeat = 2)]
def evaluate(grid,x,y):
    rID = x + 10; pLV = grid + rID * y
    return int(f"{pLV*rID:03d}"[-3]) - 5
def find_level(x,y,i):
    return sum(pts[(x+u,y+v)] for (u,v) in double_range(0, i))
def find_max(pts, i = 3):
    return max({(*pair, i): find_level(*pair, i) for pair in
        double_range(1, 301 - i)}.items(), key = lambda xs: xs[1])
pts = {pair: evaluate(8141, *pair) for pair in double_range(1, 301)}
last_max, _ = 0, print('Silver: %s with %d' % find_max(pts, 3))
for j in range(1, int(301**0.5)+1):
    coords, val = find_max(pts, j)
    if val > last_max:
        print('Option:',coords,'with', val)
        last_max = val
