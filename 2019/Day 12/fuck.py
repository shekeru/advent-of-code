from itertools import combinations
import numpy as np; import math, re
# Shit Hawk Moons
class Moon:
    def __init__(st, ln):
        xs = map(int, re.findall(r'-?\d+', ln))
        st.position, st.velocity = \
            map(np.array, ([*xs], [0] * 3))
    def __sub__(st, pt):
        return st.position - pt.position
    def total(st):
        fn = lambda xs: sum(map(abs, xs))
        return fn(st.position) * fn(st.velocity)
    def hash(st):
        return (*map(hash, zip(st.position, st.velocity)),)
# Jupiter System
class System:
    def __init__(s, fn):
        s.list = [*map(Moon, open('2019/Day 12/' +fn))]
        s.pairs, s.counter = [*combinations(s.list, 2)], 0
        s.zeroes, s.ticks = (*s.values(),), [0] * 3
    def Update(s):
        s.counter += 1; fn = \
    lambda v: max(min(v, 1), -1)
        for st, pt in s.pairs:
            offset = [*map(fn, pt - st)]
            st.velocity += offset
            pt.velocity -= offset
        for st in s.list:
            st.position += st.velocity
            yield st.total()
        for i, v in enumerate(s.values()):
            if v == s.zeroes[i] and not s.ticks[i]:
                s.ticks[i] = s.counter
    def Solve(s, N = 1000):
        while True:
            value = sum(s.Update())
            if s.counter == N: yield value;
            if s.counter >= N and all(s.ticks):
                a, b, c = s.ticks; yield a * b * c \
            // math.gcd(a, b) // math.gcd(b, c)
    def values(s):
        return map(hash, zip(*(st.hash() for st in s.list)))
# Fuck you Eric Wastl
local = System('ins.txt').Solve()
print("Silver:", next(local))
print("Gold:", next(local))
