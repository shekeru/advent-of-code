from math import *
def FN(St, Pt):
    cf = Pt[0] - St[0], Pt[1] - St[1]
    return (pi - atan2(*cf), hypot(*cf), 100*Pt[0]+Pt[1])
xs = [(x, y) for y, ln in
    enumerate(open('2019/Day 10/ins.txt'))
for x, o in enumerate(ln) if o == '#']
ys = {St: {k: v for k,_,v in sorted((FN(St, Pt) for
    Pt in xs if St != Pt), reverse = 1)} for St in xs}
St = ys[max(ys, key = lambda x: len(ys[x]))]
print(f"Silver: {len(St)}",
    f"Gold: {St[sorted(St)[199]]}", sep='\n')
