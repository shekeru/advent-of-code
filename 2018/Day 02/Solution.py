import string, itertools
letters = string.ascii_lowercase
with open('input.txt') as f:
    xs = f.read().splitlines()
def count(x):
    return {x.count(c) for c in letters} & {2,3}
def solve(xs):
    for i in range(len(xs)-1):
        for j in range(i, len(xs)):
            match = xor(xs[i], xs[j])
            if match:
                return match
def xor(a,b):
    mark = -1
    for i in range(len(a)):
        if a[i] != b[i]:
            if mark < 0:
                mark = i
            else:
                return
    if mark >= 0:
        return a[:mark] + b[mark+1:]
cmb = [*itertools.chain(*map(count,xs))]
print('part 1:', cmb.count(2) * cmb.count(3))
print('part 2:', solve(xs))
