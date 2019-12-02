with open("2019/Day 02/input.txt") as f:
    xs = [int(x) for x in f.read().split(',')]

def p_alarm(xs, n = 12, v = 2):
    j, xs = 0, xs.copy()
    xs[1], xs[2] = n, v
    while xs[j] != 99:
        op, a, b, c = xs[j:j+4]
        if op & 1:
            xs[c] = xs[a] + xs[b]
        else:
            xs[c] = xs[a] * xs[b]
        j += 4
    return xs[0]

def fd_pr(TARGET = 19690720):
    pkt = [12, 2]
    for i in range(2):
        while True:
            y = p_alarm(xs, *pkt)
            if y <= TARGET:
                pkt[i] += 1
            else:
                pkt[i] -= 1
                break
    pkt[0] *= 100
    return sum(pkt)

print("Silver:", p_alarm(xs))
print("Gold:", fd_pr())
