import re, math
# List of Coordinates
with open('2018/Day 23/input.txt') as File:
    System = [*map(lambda Ln: tuple(map(int,
        re.findall(r'-?\d+', Ln))), File)]
# Distance Function
def Manhattan(Xs, Ys = (0, 0, 0)):
    Fn = lambda x, y: abs(y - x); return sum \
        (Fn(*Pair) for Pair in zip(Xs[:3], Ys))
# Fucking Part 2 Garbage
Limit, Values, Largest = math.inf, set(), \
    max(System, key = lambda Pt: Pt[3])
for Pt in System:
    if (Dist := Manhattan(Pt)) > Pt[3]:
        Values.add(Dist - Pt[3])
    Limit = min(Limit, Dist + Pt[3])
# Print Results
print("Silver:", sum(1 for Pt in System if
    Manhattan(Largest, Pt) <= Largest[3]))
print("Gold:", max(Pt for Pt in
    Values if Pt <= Limit))
