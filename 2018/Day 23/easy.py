from collections import defaultdict; import re
with open('input.txt') as f:
    parse = lambda x: [*map(int, re.findall(r'-?\d+', x))]
    xs = [*map(parse, f.read().splitlines())]
def m_dist(xs, ys):
    solve = lambda x, y: abs(y - x)
    return sum(solve(*pts) for pts in zip(xs[:3], ys[:3]))
def m_point(xs, ys):
    solve = lambda x, y: (y*xs[3] + x*ys[3]) / (xs[3] + ys[3])
    return [solve(*pts) for pts in zip(xs[:3], ys[:3])] + [(xs[3] + ys[3]) / 2]
st = max(xs, key = lambda x: x[3])
print("Silver:", len([x for x in xs if
    m_dist(st, x) <= st[3]]))
# Fucking Part 2 Garbage
print("Now conducting initial scan")
limit = max(x[3] for x in xs)
steps = min(x[3] for x in xs)//8
sets = defaultdict(lambda: defaultdict(int))
for x in range(-limit, limit+1, 1+steps):
    for y in range(-limit, limit+1, 1+steps):
        for z in range(-limit, limit+1, 1+steps):
            n = len([t for t in xs if m_dist([x,y,z], t) <= t[3]])
            sets[0][x] += n; sets[1][y] += n; sets[2][z] += n
print("Now optimizing...")
for _ in range(20):
    l = defaultdict(lambda: defaultdict(int))
    for k in sets:
        pts = sorted(sets[k].items(), reverse = True, key = lambda x: x[1])[:4]
        l[k][0], l[k][1] = min(a for a,b in pts), max(a for a,b in pts)
    sets = defaultdict(lambda: defaultdict(int))
    for x in range(l[0][0], l[0][1]+1, (l[0][1]-l[0][0]) // 6):
        for y in range(l[1][0], l[1][1]+1, (l[1][1]-l[1][0]) // 6):
            for z in range(l[2][0], l[2][1]+1, (l[2][1]-l[2][0]) // 6):
                n = len([t for t in xs if m_dist([x,y,z], t) <= t[3]])
                sets[0][x] += n; sets[1][y] += n; sets[2][z] += n
print("Begining descent to zero"); x,y,z = l[0][0],l[1][0],l[2][0]
init, last = len([t for t in xs if m_dist([x,y,z], t) <= t[3]]), (x,y,z)
for d in [-1000*1000, -1000*100, *range(-10000, 0)]:
    x1 = x-d if x<0 else x+d; xt = len([t for t in xs if m_dist([x1,y,z], t) <= t[3]])
    if xt == init:
        x = x1
    y1 = y-d if y<0 else y+d; yt = len([t for t in xs if m_dist([x,y1,z], t) <= t[3]])
    if yt == init:
        y = y1
    z1 = z-d if z<0 else z+d; zt = len([t for t in xs if m_dist([x,y,z1], t) <= t[3]])
    if zt == init:
        z = z1
    if last == (x,y,z):
        break
    last = (x,y,z)
print(init, m_dist([x,y,z], [0,0,0]))
