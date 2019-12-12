import numpy as np
import itertools, re
# Shit Hawk Moons
class Moon:
    def __init__(st, ln):
        xs = map(int, re.findall(r'-?\d+', ln))
        st.position, st.velocity = \
            map(np.array, ([*xs], [0] * 3))
    def __sub__(st, pt):
        return st.position - pt.position
    def __repr__(st):
        return f"{st.position} => {st.velocity}"
    @property
    def total(st):
        fn = lambda xs: sum(map(abs, xs))
        return fn(st.position) * fn(st.velocity)
# Jupiter System
class System:
    def __init__(s, fn):
        s.list = [*map(Moon, open('2019/Day 12/' +fn))]
        s.pairs = [*itertools.combinations(s.list, 2)]
    def Update(s):
        fn = lambda v: max(min(v, 1), -1)
        for st, pt in s.pairs:
            offset = [*map(fn, pt - st)]
            st.velocity += offset
            pt.velocity -= offset
        for st in s.list:
            st.position += st.velocity
            yield st.total
    def Settle(s, n = 1000):
        for x in range(n):
            v = sum(s.Update())
        return v
# Fuck you Eric Wastl
jupiter = System('ins.txt')
print("Silver:", jupiter.Settle())
