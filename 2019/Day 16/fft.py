from itertools import *
# Functions
def to_int(xs):
    return int("".join(map(str, xs)))
base = (0, 1, 0, -1)
def coeff(N, Idx):
    return base[(Idx+1) // (N+1) % 4]
def nth(arr, Y = 100):
    for i in range(Y):
        arr = [*fft(arr)]
    return to_int(arr[:8])
def fft(arr):
    for N in range(len(arr)):
        digit = sum(x * coeff(N, i) for i,x in enumerate(arr))
        yield abs(digit) % 10
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
print("Silver:", nth(XVS))
print("Gold:", n2_fft(XVS))
