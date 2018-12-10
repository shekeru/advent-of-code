import re, itertools, matplotlib.pyplot as plt
with open('input.txt') as f:
    parse = lambda x: tuple(map(int, re.findall(r'-?\d+', x)))
    points = [*map(parse, f.read().splitlines())]
def yield_all(points):
    for i in itertools.count():
        yield (i, [(a + c * i, b + d * i) for (a,b,c,d) in points])
def lowest_bounds(points):
    generator = yield_all(points)
    (_, state) = next(generator)
    for j, trans in generator:
        current = sum(map(area, zip(*trans)))
        last = sum(map(area, zip(*state)))
        if current > last:
            return (state, j-1)
        state = trans
bounds, area = lambda xs: (min(xs), max(xs)+1), lambda xs: max(xs) - min(xs)
data, index = lowest_bounds(points); xs, ys = map(bounds, zip(*data))
index, plt.imshow([
    [1 if (x,y) in data else 0 for x in range(*xs)]
for y in range(*ys)], cmap="cool")
