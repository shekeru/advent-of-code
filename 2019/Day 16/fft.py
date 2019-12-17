# Part1 Functions
def to_int(xs):
    return int("".join(map(str, xs)))
def fft_a(v, i):
    sign, s = 1, i + 1
    j, length = i, len(v)
    while j < len(v):
        yield sum(v[j:j+s]) * sign
        j += 2 * s; sign = -sign
def part1(v, N = 100):
    for x in range(N):
        v = [abs(sum(fft_a(v, i))) % 10
            for i in range(len(v))]
    return to_int(v[:8])
# works because offset > n/2
def n2_fft(xs, Y = 100):
    v = (xs*10000)[to_int(xs[:7]):]
    for _ in range(Y):
        for x in range(-2, -len(v)-1, -1):
            v[x] = (v[x]+v[x+1]) % 10
    return to_int(v[:8])
# Read Input
with open('2019/Day 16/ins.txt') as f:
    XVS = [*map(int, f.read().strip())]
# Display
print("Silver:", part1(XVS))
print("Gold:", n2_fft(XVS))
