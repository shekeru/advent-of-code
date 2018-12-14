class WriteChecks(dict):
    def __setitem__(s, key, value):
        if key in s:
            super().__setitem__(key, (0,0,0))
            #if 'f' not in dir(s): s.f =
            print("Silver:",
                "First impact at ({1},{0})".format(*key))
        else: super().__setitem__(key, value)
with open('input.txt') as f:
    tracks = [*map(list, f.read().splitlines())]
carts, conv = WriteChecks(), {'>': (0,1), '<': (0,-1), '^': (-1, 0), 'v': (1, 0)}
for y in range(len(tracks)):
    for x in range(len(tracks[y])):
        if tracks[y][x] in conv.keys():
            carts[y,x] = (*conv[tracks[y][x]], 0)
            tracks[y][x] = '-' if tracks[y][x] in ['>','<'] else '|'
print(len(carts))
def run_system():
    for y,x in sorted(carts):
        if 1 is len([*filter(sum, carts.values())]):
            print(f'Gold: Last cart at ({x},{y})'); return True
        h, d, t = carts[y,x]
        if tracks[y][x] in ['|', '-']:
            carts[y+h, x+d] = (h,d,t)
        elif tracks[y][x] == '/':
            carts[y-d, x-h] = (-d,-h,t)
        elif tracks[y][x] == '\\':
            carts[y+d, x+h] = (d,h,t)
        elif tracks[y][x] == '+':
            if t%3 == 0: # Left?
                carts[y-d, x+h] = (-d,h,t+1)
            if t%3 == 1: # Ahead?
                carts[y+h, x+d] = (h,d,t+1)
            if t%3 == 2: # Right?
                carts[y+d, x-h] = (d,-h,t+1)
        del carts[y, x]
while(not run_system()):
    pass
