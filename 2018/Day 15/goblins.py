from typing import NamedTuple
import collections

class Point(NamedTuple('Pt', [('y', int), ('x', int)])):
    def __add__(self, offset):
        return type(self)(self.y + offset.y, self.x + offset.x)
    @property
    def nb4(self):
        return [self + o for o in map(lambda xs: Point(*xs),
            [(-1, 0), (0, -1), (0, 1), (1, 0)])]
    
class Unit:
    def __init__(self, elf, pt, dmg, hp = 200):
        self.elf, self.pt, self.hp = elf, pt, hp
        self.dmg = 3 if not elf else dmg
    def alive(self):
        if self.hp <= 0:
            if self.dmg > 3:
                raise Exception('elf_died')
            return False
        return True
    
class World(dict):
    def __init__(self, name, elf_dmg = 3):
        # WorldSpace Dict, and Entity List
        self.units, self.name = [], name
        self.dmg = elf_dmg; super()
        # Read from file
        with open(name) as f:
            lines = [*map(list, f.read().splitlines())]
            for y, line in enumerate(lines):
                for x, char in enumerate(line):
                    self[Point(y, x)] = char != '#'
                    if char in "GE":
                        self.units.append(Unit(
                            char == 'E', Point(y, x),
                            dmg = elf_dmg))
    # Crude Pathing (Some sort of Dijkstra's)
    def next_move(self, unit, targets):
        spaces, paths = collections.deque([unit.pt]), {unit.pt: []}
        slots = {pt for v in targets for pt in v.pt.nb4 if self.valid(pt)}
        while spaces:
            current = spaces.popleft()
            if current in slots:
                yield from (paths[current] or [current])
            for future in current.nb4:
                if future not in paths and self.valid(future):
                    paths[future] = paths[current] + [future]
                    spaces.append(future)
    def valid(self, point):
        return self[point] and point not in self.active
    # Main Logic by Unit
    def on_turn(self, unit):
        # Update all others/enemies
        targets = [v for v in self.units if v.elf != unit.elf and v.alive()]
        # None to Fight
        if not targets:
            return True
        # Select New Position
        self.active = {v.pt for v in self.units if v.alive() and v != unit}
        for crds in self.next_move(unit, targets):
            unit.pt = crds; break
        # Select Favored Target
        opponents = [v for v in targets if v.pt in unit.pt.nb4]
        if opponents:
            target = min(opponents, key = lambda v: (v.hp, v.pt))
            target.hp = max(0, target.hp - unit.dmg)
    # Run All Unit Turns
    def fight_all(self):
        for unit in sorted(self.units, key = lambda x: x.pt):
            if unit.alive():
                if self.on_turn(unit):
                    return True
    # Multipart score
    def get_score(self):
        try:
            i = 0
            while not self.fight_all():
                i += 1
            #print(self.dmg, i, sum(map(lambda v: v.hp, self.units)))
            return i * sum(map(lambda v: v.hp, self.units))
        except Exception as eff:
            if 'elf_died' in eff.args:
                return World(self.name, self.dmg + 1).get_score()
    
print("Running part 1 tests...")
assert(27730 == World("test0.txt").get_score())
assert(36334 == World("test1.txt").get_score())
assert(39514 == World("test2.txt").get_score())
assert(27755 == World("test3.txt").get_score())
assert(28944 == World("test4.txt").get_score())
assert(18740 == World("test5.txt").get_score())
print("Silver: %d" % World("input.txt").get_score())
assert(4988 == World("test0.txt", 4).get_score())
assert(31284 == World("test2.txt", 4).get_score())
assert(3478 == World("test3.txt", 4).get_score())
assert(6474 == World("test4.txt", 4).get_score())
assert(1140 == World("test5.txt", 4).get_score())
print("Gold: %d" % World("input.txt", 48).get_score())
