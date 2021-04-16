lines = [(x[0], int(x[1:])) for
    x in open('2020/Day 12/input.txt')]
# Silver
dirs, actions = 'NESW', {
    'N': lambda h, x, y, f: (h, x, y + f),
    'E': lambda h, x, y, f: (h, x + f, y),
    'S': lambda h, x, y, f: (h, x, y - f),
    'W': lambda h, x, y, f: (h, x - f, y),
    'R': lambda h, x, y, f: ((h + f) % 360, x, y),
    'L': lambda h, x, y, f: ((h - f) % 360, x, y),
    'F': lambda h, x, y, f: actions[dirs[h // 90]](h, x, y, f),
}
# Run Silver
state = 90, 0, 0
for op, force in lines:
    state = actions[op](*state, force)
print('silver:', sum(map(abs, state[-2:])))
# Gold
actions = {
    'N': lambda a, b, x, y, f: (a, b + f, x, y),
    'E': lambda a, b, x, y, f: (a + f, b, x, y),
    'S': lambda a, b, x, y, f: (a, b - f, x, y),
    'W': lambda a, b, x, y, f: (a - f, b, x, y),
    'R': lambda a, b, x, y, f: actions['R'](b, -a, x, y, f - 90) if f else (a, b, x, y),
    'L': lambda a, b, x, y, f: actions['L'](-b, a, x, y, f - 90) if f else (a, b, x, y),
    'F': lambda a, b, x, y, f: (a, b, x + a * f, y + b * f),
}
# Run Gold
state = 10, 1, 0, 0
for op, force in lines:
    state = actions[op](*state, force)
print('gold:', sum(map(abs, state[-2:])))
