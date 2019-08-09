# Global State
states = dict()
# Functions
def erode(x, y):
    if not (x,y) or (x,y) == target:
        value = 0
    elif not y:
        value = x * 16807
    elif not x:
        value = y * 48271
    else:
        value = states[x-1, y] * states[x, y-1]
    states[x, y] = (value + depth) % 20183
    return states[x, y]
# Run Problem
depth, target = 3879, (8, 713)
silver = sum(erode(x,y) % 3 for x in
    range(target[0]+1) for y in range(target[1]+1))
print("Silver:", silver)
