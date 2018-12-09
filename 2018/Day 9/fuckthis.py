import collections
class Node:
    def __init__(s, x = 0):
        s.next = s; s.prev = s; s.val = x
    def insert(s, x):
        a = s.next; b = a.next; a.next = Node(x)
        a.next.next = b; a.next.prev = a
        b.prev = a.next; return a.next
    def knockout(s, x):
        m = s.prev
        for _ in range(7):
            m = m.prev
        t = m.next; m.next = t.next
        m.next.prev = m; return (m.next, x+t.val)
def solve_advent(players, limit):
    sets, scores = Node(), collections.defaultdict(int)
    show = lambda: scores[max(scores, key = scores.get)]
    for x in range(1, 1+limit*100):
        if x % 23:
            sets = sets.insert(x)
        else:
            sets, pops = sets.knockout(x)
            scores[x % players] += pops
        if x == limit:
            print("Silver:", show())
    print("Gold:", show())
solve_advent(428, 72061)
