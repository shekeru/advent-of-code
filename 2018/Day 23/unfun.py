import re, queue
with open('2018/Day 23/input.txt') as f:
    parse = lambda x: [*map(int, re.findall(r'-?\d+', x))]
    sys = [*map(parse, f.read().splitlines())]
def m_dist(xs, ys):
    solve = lambda x, y: abs(y - x)
    return sum(solve(*pts) for pts in zip(xs[:3], ys[:3]))
st = max(sys, key = lambda pt: pt[3])
print("Silver:", len([pts for pts in sys if
    m_dist(st, pts) <= st[3]]))
# Fucking Part 2 Garbage
pq = queue.PriorityQueue()
for ys in sys:
    dist = m_dist((0, 0, 0), ys)
    pq.put((max(0, dist - ys[3]), 1))
    pq.put((1 + dist + ys[3], -1))
result, n, last = 0, 0, 0
while not pq.empty():
    dist, delta = pq.get()
    n += delta
    if n > last:
        last = n
        result = dist
print("Gold:", result)
