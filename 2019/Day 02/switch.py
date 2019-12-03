from operator import add, mul
with open("2019/Day 02/input.txt") as f:
    xs = [int(x) for x in f.read().split(',')]

def p_alarm(xs, n = 12, v = 2):
    j, xs = 0, xs.copy()
    xs[1], xs[2] = n, v
    while xs[j] != 99:
        op, a, b, c = xs[j:j+4]
        fn = add if op & 1 else mul
        xs[c] = fn(xs[a], xs[b])
        j += 4
    return xs[0]

def fd_pr(TARGET = 19690720):
    base = p_alarm(xs, *[0]*2)
    n, v = divmod(TARGET - base,
        p_alarm(xs, 1, 0) - base)
    return n * 100 + v

print("Silver:", p_alarm(xs))
print("Gold:", fd_pr())
