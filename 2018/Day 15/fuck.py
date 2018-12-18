import itertools
with open('2018/Day 15/input.txt') as f:
    space = [*map(list, f.read().splitlines())]
search = [(-1, 0), (0, -1), (0, 1), (1, 0)]
class System:
    def __init__(s, val = 3):
        s.i, s.units, s.e = 0, dict(), 0
        for y in range(len(space)):
            for x in range(len(space[y])):
                if space[y][x] == "G":
                    s.units[y,x] = ["G", 200, 3]
                if space[y][x] == "E":
                    s.units[y,x] = ["E", 200, val]
                    s.e += 1
    def collides(s, y, x, u, v):
        try:
            return (space[y][x] == '#' or
                (s.units.get((y,x)) and (y,x) != (u,v)))
        except:
            return True
    def attack_stage(s, y,x):
        for u,v in sorted(((y+a,x+b) for a,b in search if s.units.get((y+a,x+b))), key = lambda xs: s.units[(*xs,)][1]):
            unit, target = s.units[y,x], s.units.get((u,v), ["N", 0])
            if target[1] > 0 and target[0] != unit[0]:
                s.units[u,v][1] -= unit[2]
                if s.units[u,v][1] <= 0:
                    del s.units[u,v]
                return True
    def run_system(s):
        did_attack = set()
        for y,x in sorted(s.units):
            if not s.units.get((y,x)) or (y,x) in did_attack: # Was killed?
                continue
            if s.attack_stage(y,x):
                did_attack.add((y,x))
                continue
            stage1 = [s.search_field(y,x,*pts) for pts in s.get_enemies(s.units[y,x])]
            if not stage1:
                return
            stage2 = [xs for xs in stage1 if xs]; stage3 = [x[0] for x in stage2 if len(x) == min(map(len, stage2))]
            for shift in sorted(stage3):
                s.units[(*shift,)] = s.units[y,x]
                del s.units[y,x]; y,x = shift
                break
            if s.attack_stage(y,x):
                did_attack.add((y,x))
                continue
        return True
    def get_enemies(s,t):
        return (k for k in sorted(s.units) if s.units[k][0] != t[0])
    def search_field(s,y,x,y1,x1):
        field = {(y,x): 0}
        while (y1,x1) not in field:
            length = len(field)
            for y,x in sorted(field):
                for u,v in search:
                    if (y+u, x+v) not in field and not s.collides(y+u,x+v,y1,x1):
                        field[y+u,x+v] = field[y,x] + 1
            if length == len(field):
                return list()
        d, y0, x0 = min((field[y1+u,x1+v], y1+u, x1+v) for u,v in search
            if (y1+u,x1+v) in field); path = [(y0, x0)]
        for j in range(d-1, 0, -1):
            for u,v in search:
                if field.get((y0+u,x0+v)) == j:
                    path.append((y0+u, x0+v))
                    y0, x0 = y0+u, x0+v; break
        return [*reversed(path)]
    def get_score(s):
        while s.run_system():
            s.i += 1
        return s.i * sum(map(lambda x: x[1], s.units.values()))
    def cmp_elves(s):
        score = s.get_score()
        if s.e == sum([1 for x in s.units.values() if x[0] == 'E']):
            return score
print('Silver:', System().get_score())
#for i in itertools.count(16):
fuck = System(16)
fuck.get_score()
#if score:
print('Gold:', score)
fuck.units
