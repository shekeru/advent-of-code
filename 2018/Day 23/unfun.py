from collections import defaultdict
from random import randint
import re
with open('input.txt') as f:
    parse = lambda x: [*map(int, re.findall(r'-?\d+', x))]
    sys = [*map(parse, f.read().splitlines())]
def m_dist(xs, ys):
    solve = lambda x, y: abs(y - x)
    return sum(solve(*pts) for pts in zip(xs[:3], ys[:3]))
st = max(sys, key = lambda pt: pt[3])
print("Silver:", len([pts for pts in sys if
    m_dist(st, pts) <= st[3]]))
# Fucking Part 2 Garbage
print(m_dist((11008975, 28886116, 46356905), (0,0,0)))
xs, ys, zs, rs = zip(*sys); steps, sig = dict([
    ((11008974, 28886114, 46356904), 915),
    ((11008975, 28886116, 46356905), 915),
    ((11008978, 28886123, 46356910), 913),
    ((11008823, 28885334, 46356274), 912),
    ((11023345, 28959806, 46416223), 909),
    ((10353702, 28308607, 46434704), 901),
    ((9745043, 27929441, 46664178), 898),
    ((9745043, 28086255, 46820970), 895),
    ((11008807, 28886193, 46357334), 887),
    ((11589915, 28828700, 46469185), 880),
]), sum(rs)//len(rs)//10
inits =[(min(n), max(n)) for n in [xs,ys,zs]]
global_entropy = lambda: [randint(*n) for n in inits]
for lvl in range(50):
    # Retry Keys
    for x,y,z in list(steps.keys()):
        x += randint(-1,0); y += randint(-1,0); z += randint(-1,0)
        steps[x,y,z] = len([pts for pts in sys if m_dist([x,y,z], pts) <= pts[3]])
    # General Descent [1000]
    #for x in range(min(xs), max(xs)+1, 1+(max(xs)-min(xs))//10):
    #    for y in range(min(ys), max(ys)+1, 1+(max(ys)-min(ys))//10):
    #        for z in range(min(zs), max(zs)+1, 1+(max(zs)-min(zs))//10):
    #            steps[x,y,z] = len([pts for pts in sys if m_dist([x,y,z], pts) <= pts[3]])
    # Local Entropy [1000]
    for _ in range(1000):
        x,y,z = [randint(min(n)-10000, max(n)+10000) for n in [xs,ys,zs]]
        steps[x,y,z] = len([pts for pts in sys if m_dist([x,y,z], pts) <= pts[3]])
    # Random Entropy [150]
    for _ in range(150):
        x,y,z = global_entropy()
        steps[x,y,z] = len([pts for pts in sys if m_dist([x,y,z], pts) <= pts[3]])
    steps, best200 = {}, sorted(steps.items(), reverse=True, key = lambda x: x[1])[:125]
    xs, ys, zs = zip(*(b[0] for b in best200)); steps = dict(best200)
    print(f"Level: {lvl} Optimal: {best200[:5]}")
