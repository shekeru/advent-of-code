from operator import itemgetter, attrgetter
from math import atan2, pi, hypot
# Position Object
class Pt(list):
    def __init__(s, x, y):
        s.value = y + x * 100
        s.x, s.y = x, y
    def __sub__(s, pt):
        return (pt.x - s.x, pt.y - s.y)
    def laser(s, n = 200):
        ys = {k: v for k,_,v in s}
        return ys[sorted(ys)[n-1]]
    def refresh(s):
        for pt in Pt.Field:
            if pt is not s:
                offset = s - pt; theta = atan2(*offset)
                yield (pi - theta, hypot(*offset), pt.value)
    def Identify(field):
        Pt.Field = (*field,)
        for pt in Pt.Field:
            pt += sorted(pt.refresh(), reverse = True)
            pt.targets = len({*map(itemgetter(0), pt)})
        return max(Pt.Field, key = attrgetter('targets'))
# Read Asteroid Grid
Station = Pt.Identify(Pt(x, y) for y, ln
    in enumerate(open('2019/Day 10/ins.txt'))
for x, o in enumerate(ln) if o == '#')
# Display Results
print("Silver:", Station.targets)
print("Gold:", Station.laser())
