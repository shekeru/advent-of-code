from itertools import *
# Functions
def coeff(N, Idx):
    return base[(Idx+1) // (N+1) % 4]
def nth(arr, Y = 100):
    for _ in range(Y):
        arr = [*fft(arr)]
    return "".join(map(str, arr))
def fft(arr):
    for N in range(len(arr)):
        digit = sum(x * coeff(N, i) for i,x in enumerate(arr))
        yield abs(digit) % 10
# Read Input
with open('2019/Day 16/ins.txt') as f:
    XVS = [*map(int, f.read().strip())]
# Display
print(nth(XVS)[:8])
#print(nth(XVS, 10000)[:8])

base = (0, 1, 0, -1)
arr = [1,2,3,4,5,6,7,8]
