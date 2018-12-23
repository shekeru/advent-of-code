x0, y0 = 8,713
depth = 3879
# Logic
states, yc, xc = {
    (x0, y0): depth % 20183,
    (0,0): depth % 20183,
}, 16807, 48271
def calculate(x, y):
    if states.get((x,y)):
        return
    if not y:
        temp = x * yc
    elif not x:
        temp = y * xc
    else:
        temp = states[x-1, y] * states[x, y-1]
    states[x, y] = (temp + depth) % 20183
for y in range(y0+1):
    for x in range(x0+1):
        calculate(x, y)
sum(s%3 for s in states.values())
