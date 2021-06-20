import re, queue
# List of Coordinates
with open('2018/Day 23/input.txt') as File:
    System = [*map(lambda Ln: tuple(map(int,
        re.findall(r'-?\d+', Ln))), File)]
# Distance Function
def Manhattan(Xs, Ys = (0, 0, 0)):
    Fn = lambda x, y: abs(y - x); return sum \
        (Fn(*Pair) for Pair in zip(Xs[:3], Ys))
# Silver Was Easy
Largest = max(System, key = lambda Pt: Pt[3])
print("Silver:", sum(1 for Pt in System if
    Manhattan(Largest, Pt) <= Largest[3]))
# Fucking Part 2 Garbage
Queue = queue.PriorityQueue()
for Dist, Pt in map(lambda x: (Manhattan(x), x), System):
    Queue.put((max(0, Dist - Pt[3]), 1))
    Queue.put((1 + Dist + Pt[3], -1))
Shortest, Total, Maximum = 0, 0, 0
# Something I Don't Understand
while not Queue.empty():
    Distance, Delta = Queue.get(); Total += Delta
    if Total > Maximum:
        Shortest, Maximum = Distance, Total
print("Gold:", Shortest)
