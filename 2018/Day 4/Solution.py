import re, collections
fuckshit = r'\[(.+)(?:\].*?(#\d+|wakes|falls))'
with open('input.txt') as f:
    xs = re.findall(fuckshit, f.read())
actions = sorted(xs, key = lambda x: x[0])
guards = collections.defaultdict(
    lambda: collections.defaultdict(int)
); active, start = "", int()
for t, action in actions:
    if "wakes" in action:
        for k in range(start, int(t[-2:])):
            guards[active][k] += 1
    elif "falls" in action:
        start = int(t[-2:])
    elif "#" in action:
        active = int(action[1:])
def solve(matrix, func):
    alpha = max(matrix, key = lambda k:
        func(matrix[k].values())
    ); beta = max(matrix[alpha], key =
        matrix[alpha].get
    ); return alpha * beta
def dict_seq(start):
    result = collections.defaultdict(dict)
    for k in start:
        for m in start[k]:
            result[m][k] = start[k][m]
    return result
print('part 1:', solve(guards, sum))
print('part 2:', solve(dict_seq(guards), max))
