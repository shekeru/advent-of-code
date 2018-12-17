from operator import *
import re, itertools, collections
with open('2018/Day 16/input.txt') as f:
    parse, st = lambda x: list(map(int, re.findall(r'\d+', x))), lambda a,b: a
    trans, system = map(lambda x: x.splitlines(), f.read().split("\n"*4))
trans, system = [[*map(parse, t)] for v,t in itertools.groupby(
    trans, lambda x: x == '') if not v], [*map(parse, system)]
def ri(*xs):
    for x in xs: yield from ((x, True, True), (x, True, False))
def ir(*xs):
    for x in xs: yield (x, False, True)
def isolate(mapped):
    for k, vs in mapped.items():
        if len(vs) == 1:
            mapped[k] = vs.pop()
            for sets in mapped.values():
                if isinstance(sets, set):
                    sets.discard(mapped[k])
    if len({*map(type, mapped.values())}) > 1:
        isolate(mapped)
def evaluate(op, xs, t, ys):
    return execute(xs.copy(), *op, *t[1:]) == ys
def execute(xs, op, r1, r2, i, v, l):
    xs[l] = op(xs[i] if r1 else i, xs[v]
        if r2 else v); return xs
operators = [*ri(add,mul,and_,or_,gt,eq), *ir(gt,eq,st), (st, True, False)]
state, matches, mapped ,  = [0] * 4, [(sets[1][0],
    [op for op in operators if evaluate(op,*sets)]
) for sets in trans], collections.defaultdict(list)
print('Silver:', len([*filter(lambda x: len(x[1]) > 3, matches)]))
for k, vs in matches:
    mapped[k].append(vs)
for i, sets in mapped.items():
    mapped[i] = {op for seq in sets for op in
seq if all(map(lambda x: op in x, sets))}
isolate(mapped)
for op, *ts in system:
    execute(state, *mapped[op], *ts)
print('Gold:', state[0])
