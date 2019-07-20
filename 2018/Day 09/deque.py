from collections import deque, defaultdict
def solve_advent(players, limit):
    sets, scores = deque([0]), defaultdict(int)
    for x in range(1, 1 + limit*100):
        if x % 23:
            sets.rotate(-2)
            sets.appendleft(x)
        else:
            sets.rotate(7)
            scores[x % players] += x + sets.popleft()
        if x == limit:
            print("Silver:", max(scores.values()))
    print("Gold:", max(scores.values()))
solve_advent(428, 72061)
