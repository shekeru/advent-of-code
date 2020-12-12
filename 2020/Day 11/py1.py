import itertools; Map = {}
Deltas = [*itertools.product((0, -1, 1), repeat = 2)][1:]
for Y, Ln in enumerate(open('Day 11/input.txt')):
     for X, Ch in enumerate(Ln.strip()):
         Map[Y, X] = Ch
# Fuck you Eric
class System:
    def __init__(s, Map, Mode = 4):
        s.Map, s.Mode = Map.copy(), Mode
    def Check(s, y, x, a, b):
        y += a; x += b
        Ch = s.Past.get((y, x), '')
        if s.Mode < 5 or Ch in '#L':
            return Ch == "#"
        return s.Check(y, x, a, b)
    def Step(s, Value = 0):
        s.Past = s.Map.copy()
        for Pt, Ch in s.Past.items():
            Factor = len([*filter(None, (s.Check(*Pt, *Dt) for Dt in Deltas))])
            if Ch == "L" and not Factor:
                s.Map[Pt] = '#'
            if Ch == "#" and Factor >= s.Mode:
                s.Map[Pt] = 'L'
        NewVal = len([*filter(lambda x: x == '#', s.Map.values())])
        return Value if NewVal == Value else s.Step(NewVal)
# Resultss
print("Silver:", System(Map).Step())
print("Gold:", System(Map, 5).Step())
