import re, string, itertools
with open('input.txt') as f:
    parse = lambda x: tuple(re.findall(r'[A-Z]', x)[1:])
    routes = [*map(parse, f.read().splitlines())]
def value_seconds(letter, offset):
    return string.ascii_uppercase.find(letter) + offset
def double_map(routes):
    return {chr: set() for line in routes for chr in line}
def forwards(routes, workers = 2, offset = 0):
    accum, queue, table = "", dict(), double_map(routes)
    for (req, key) in routes:
        table[key].add(req)
    for seconds in itertools.count():
        queue = {k: v-1 for k,v in queue.items()}
        for worker in queue.copy():
            if queue[worker] < 1:
                for rest in table.copy():
                    table[rest].discard(worker)
                accum += worker; del queue[worker]
        nexts = [*sorted(k for k,v in table.items() if not v)]
        for i in range(min(len(nexts), workers - len(queue))):
            queue[nexts[i]] = (value_seconds(nexts[i],offset+1) if
                isinstance(offset, int) else 0); del table[nexts[i]]
        if not len(table)+len(queue):
            return (seconds, accum)
print('part 1:', forwards(routes, workers = 1, offset = None))
print('part 2:', forwards(routes, workers = 5, offset = 60))
