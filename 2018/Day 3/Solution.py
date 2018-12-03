import re, collections
with open('input.txt') as f:
    parse = lambda x: [*map(int, re.findall(r'\d+', x))]
    xs = [*map(parse, f.read().splitlines())]
table = collections.defaultdict(int)
def apply(_, *vals):
    for k in coords(*vals):
        table[k] += 1
def coords(x, y, w, h):
    for i in range(y, y+h):
        for j in range(x, x+w):
            yield (i, j)
def search(lines):
    for (number, x, y, w, h) in lines:
        if w * h == sum(table[k] for k in
            coords(x, y, w, h)): return number
_, overlap = [apply(*line) for line in xs], sum(
    [1 for v in table.values() if v > 1]
); print('part 1:', overlap)
print('part 2:', search(xs))
