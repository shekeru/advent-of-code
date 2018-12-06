import re, collections
with open('input.txt') as f:
    parse = lambda x: tuple(map(int, re.findall(r'\d+', x)))
    points = [*map(parse, f.read().splitlines())]
result = collections.defaultdict(int)
a = min(x for x,_ in points)
b = min(y for _,y in points)
c = max(x for x,_ in points)
d = max(y for _,y in points)
corners = [(a,b),(c,b),(a,d),(c,d)]
fuck2 = int()
def m_dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)
def maybe(x, y):
    ll = [(m_dist(x,y,*p), p) for p in points+corners]
    val, p = min(ll, key = lambda x: x[0])
    if [v[0] for v in ll].count(val) == 1 and p not in corners:
        result[p] += 1
def eat_shit(x, y):
    global fuck2
    ll = sum([m_dist(x,y,*p) for p in points])
    if ll < 10000:
        fuck2 += 1
for y in range(b,d):
    for x in range(a,c):
        maybe(x, y)
        eat_shit(x, y)
print(max(result.values()), fuck2)
