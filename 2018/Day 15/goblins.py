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
    
class World(dict):
    def __init__(self, name, elf_dmg = 3):
        # WorldSpace Dict, and Entity List
        super(); self.elf_dmg = elf_dmg
        self.units, self.name = [], name
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
            for future in current.nb4:
                if future not in paths and self.valid(future):
                    paths[future] = paths[current] + [future]
                    if not {*paths} & slots: # do not break
                        spaces.append(future)
        opts = sorted({key for key in paths if key in slots},
            key = lambda pt: (len(paths[pt]), pt)) + [unit.pt]
        paths[unit.pt] = [unit.pt]; yield from paths[opts[0]]
    def valid(self, point):
        return self[point] and point not in self.active
    # Main Logic by Unit
    def on_turn(self, unit):
        targets = [v for v in self.units if v.elf != unit.elf and v.hp]
        self.active = {v.pt for v in self.units if v.hp and v != unit}
        # No enemies
        if not targets:
            return unit.dmg == self.elf_dmg
        # Move, Find Nearby, Attack, Clamp HP
        unit.pt = next(self.next_move(unit, targets))
        for target in sorted([v for v in targets if v.pt in
            unit.pt.nb4], key = lambda v: (v.hp, v.pt))[:1]:
            target.hp = max(0, target.hp - unit.dmg)
    # Simulate battle
    def fight_all(self, turns = 0):
        for unit in sorted(self.units, key = lambda x: x.pt):
            if unit.hp:
                if self.on_turn(unit):
                    return turns
            elif unit.elf and unit.dmg > 3:
                return -turns
        return self.fight_all(turns + 1)
    # Multipart score
    def get_score(self):
        turns = self.fight_all()
        if turns > 0:
            return turns * sum(v.hp for v in self.units)
        return World(self.name, self.elf_dmg + 1).get_score()
    
print("Running section 1 tests...")
assert(27730 == World("test0.txt").get_score())
assert(36334 == World("test1.txt").get_score())
assert(39514 == World("test2.txt").get_score())
assert(27755 == World("test3.txt").get_score())
assert(28944 == World("test4.txt").get_score())
assert(18740 == World("test5.txt").get_score())

print("Running section 2 tests...")
assert(4988 == World("test0.txt", 4).get_score())
assert(31284 == World("test2.txt", 4).get_score())
assert(3478 == World("test3.txt", 4).get_score())
assert(6474 == World("test4.txt", 4).get_score())
assert(1140 == World("test5.txt", 4).get_score())

print("Silver: %d" % World("input.txt").get_score())
print("Gold: %d" % World("input.txt", 4).get_score())
