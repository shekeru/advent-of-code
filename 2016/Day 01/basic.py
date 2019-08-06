# General Structures
class System:
    def __init__(self, dirs):
        self.seen, self.first = {(0, 0)}, None
        self.x, self.y, self.face = 0, 0, 0
        # Calculate Results
        for inst in dirs.split(','):
            self.step(*inst.strip())
    def step(self, t, *val):
        self.face = (self.face + (-1 if t == 'L' else 1)) % 4
        value = int(''.join(val)) * (-1 if self.face > 1 else 1)
        if self.face % 2: # West, East
            self.record(value, self.x)
            self.x += value
        else: # North, South
            self.record(value, self.y)
            self.y += value
    def record(self, delta, base):
        offset = (1 if delta > 0 else 0)
        for z in range(*sorted([base + offset, base + delta + offset])):
            location = (z, self.y) if self.face % 2 else (self.x, z)
            if not self.first and location in self.seen:
                self.first = location
            self.seen.add(location)
    def silver(self):
        return abs(self.x) + abs(self.y)
    def gold(self):
        return sum(map(abs, self.first))
# Input Formatting
def load_test(ln):
    y, xs = ln.split(':')
    return int(y), xs.strip()
# Load Test Cases/Input
with open('2016/Day 01/tests.txt') as f:
    exs = [load_test(ln) for ln in f.readlines()]
# Verify Test Cases
for r, ins in exs:
    actual = System(ins).silver()
    print("Test Case:", r, '==>', actual)
    assert(r == actual)
# Calculate Results
with open('2016/Day 01/input.txt') as f:
    world = System(f.read().strip())
print("Silver:", world.silver())
print("Gold:", world.gold())
