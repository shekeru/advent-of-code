from operator import itemgetter, attrgetter
from math import atan2, pi, hypot
# Position Object
class Pt(list):
    def __init__(s, x, y):
        s.score = y + x * 100
        s.x, s.y = x, y
    def __repr__(s):
        return repr((s.x, s.y))
    def __sub__(s, pt):
        return (s.x - pt.x, s.y - pt.y)
    def laser(s, n = 200):
        past, active = [], s.copy()
        while active:
            Last = -1
            for V in active.copy():
                Th, Dt, Ap = V
                if Th != Last:
                    past.append(Ap)
                    active.remove(V)
                    Last = Th
        return past[n - 1]
    def refresh(s):
        for pt in Pt.Field:
            if pt is not s:
                offset = s - pt; theta = atan2(*offset)
                yield (2*pi -theta if theta > 0 else
                    -theta, hypot(*offset), pt.score)
    def Identify(field):
        Pt.Field = (*field,)
        for pt in Pt.Field:
            pt += sorted(pt.refresh())
            pt.targets = len({*map(itemgetter(0), pt)})
        return max(Pt.Field, key = attrgetter('targets'))
# Read File
Station = Pt.Identify(Pt(x, y) for y, ln
    in enumerate(open('2019/Day 10/ins.txt'))
for x, o in enumerate(ln) if o == '#')
# Display Results
print("Silver:", Station.targets)
print("Gold:", Station.laser())
