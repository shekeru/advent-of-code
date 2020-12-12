import math, cmath
# Dog Aids Unified
class Cardinal:
    def N(s, V):
        s.Pt += complex(0, V)
    def S(s, V):
        s.Pt -= complex(0, V)
    def E(s, V):
        s.Pt += complex(V, 0)
    def W(s, V):
        s.Pt -= complex(V, 0)
    FN = [N, E, S, W]
# Dog Aids 1
class Silver(Cardinal):
    def __init__(s):
        s.H, s.Pt = 90, 0+0j; [getattr(s, O)(V) for O, V in Pairs]
        print("Silver:", int(sum(map(abs, (s.Pt.real, s.Pt.imag)))))
    def R(s, V):
        s.H = (s.H + V) % 360
    def L(s, V):
        s.H = (s.H - V) % 360
    def F(s, V):
        Silver.FN[s.H//90](s, V)
# Dog Aids 2
class Gold(Cardinal):
    def __init__(s):
        s.Pt, s.Sh = 10+1j, 0+0j; [getattr(s, O)(V) for O, V in Pairs]
        print("Gold:", int(sum(map(abs, (s.Sh.real, s.Sh.imag)))))
    def R(s, V):
        s.Pt = cmath.rect(abs(s.Pt), math.radians((math.degrees(cmath.phase(s.Pt)) - V) % 360))
    def L(s, V):
        s.Pt = cmath.rect(abs(s.Pt), math.radians((math.degrees(cmath.phase(s.Pt)) + V) % 360))
    def F(s, V):
        s.Sh += V * s.Pt
# Fuck you Eric
Pairs = [(LN[0], int(LN[1:])) for LN in
    open('Day 12/input.txt')]; Silver(), Gold()
