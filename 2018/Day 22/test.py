import re
def ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))  # thanks mserrano!
inp = """
depth: 3879
target: 8, 400
""".strip()
lines = inp.splitlines()
depth = ints(lines[0])[0]
tx, ty = tuple(ints(lines[1]))

dp = [[None for _ in range(ty+1000)] for _ in range(tx+1000)]
def erosion(x, y):
    if dp[x][y] is not None:
        return dp[x][y]
    geo = None
    if y == 0:
        geo = x * 16807
    elif x == 0:
        geo = y * 48271
    elif (x, y) == (tx, ty):
        geo = 0
    else:
        geo = erosion(x-1, y) * erosion(x, y-1)
    dp[x][y] = (geo + depth) % 20183
    return dp[x][y]

def risk(x, y):
    return erosion(x, y) % 3

print(sum(erosion(x, y) % 3 for x in range(tx+1) for y in range(ty+1)))

# torch = 1
import heapq
queue = [(0, 0, 0, 1)] # (minutes, x, y, cannot)
best = dict() # (x, y, cannot) : minutes

target = (tx, ty, 1)
while queue:
    minutes, x, y, cannot = heapq.heappop(queue)
    best_key = (x, y, cannot)
    if best_key in best and best[best_key] <= minutes:
        continue
    best[best_key] = minutes
    if best_key == target:
        print(minutes)
        break
    for i in range(3):
        if i != cannot and i != risk(x, y):
            heapq.heappush(queue, (minutes + 7, x, y, i))
    
    # try going up down left right
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        newx = x + dx
        newy = y + dy
        if newx < 0:
            continue
        if newy < 0:
            continue
        if risk(newx, newy) == cannot:
            continue
        heapq.heappush(queue, (minutes + 1, newx, newy, cannot))
