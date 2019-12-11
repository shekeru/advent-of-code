from cmath import phase
xs = [complex(y, x) for y, ln in
    enumerate(open('2019/Day 10/ins.txt'))
for x, o in enumerate(ln) if o == '#']
ys = {St: {k: v for k,_,v in sorted((
    (-phase(Pt - St), abs(Pt - St), int(Pt.real +Pt.imag *100))
for Pt in xs if St != Pt), reverse = 1)} for St in xs}
St = ys[max(ys, key = lambda x: len(ys[x]))]
print(f"Silver: {len(St)}", f"Gold: {St[sorted(St)[199]]}", sep='\n')
