import itertools
with open('input.txt') as f:
    parse = lambda x: 1 if x == '(' else -1
    xs = [*map(parse, f.read().strip())]
    ys = [*itertools.accumulate(xs)]
print('Silver:', ys[-1])
print('Gold:',ys.index(-1)+1)
