from itertools import groupby
import re, operator, collections
with open('2018/Day 16/input.txt') as f:
    trans, system = map(lambda x: x.splitlines(), f.read().split("\n"*4))
    parse = lambda x: list(map(int, re.findall(r'\d+', x)))
trans, system = [[*map(parse, t)] for v,t in groupby(trans,
    lambda x: x == '') if not v], [*map(parse, system)]
def evaluate(op, xs, t, ys):
    return execute(xs.copy(), *op, *t[1:]) == ys
def execute(xs, op, r1, r2, i, v, l):
    xs[l] = op(xs[i] if r1 else i, xs[v]
        if r2 else v); return xs
state, operators = [0]*4, [
    (operator.add, True, True), # addr
    (operator.add, True, False), # addi
    (operator.mul, True, True), # mulr
    (operator.mul, True, False), # muli
    (operator.and_, True, True), #banr
    (operator.and_, True, False), # bani
    (operator.or_, True, True), #borr
    (operator.or_, True, False), # bori
    (lambda a,b: a, True, None), # setr
    (lambda a,b: a, False, None), # seti
    (operator.gt, False, True), # gtir
    (operator.gt, True, False), # gtri
    (operator.gt, True, True), # gtrr
    (operator.eq, False, True), # eqir
    (operator.eq, True, False), # eqri
    (operator.eq, True, True), # eqrr
]; matches, mapped = [(sets[1][0],
    [op for op in operators if evaluate(op,*sets)]
) for sets in trans], collections.defaultdict(list)
print('Silver:', len([*filter(lambda x: len(x[1]) > 3, matches)]))
for k, vs in matches:
    mapped[k].append(vs)
for i, sets in mapped.items():
    mapped[i] = {op for seq in sets for op in seq if
        all(map(lambda x: op in x, sets))}
def isolate(mapped):
    for k, vs in mapped.items():
        if len(vs) == 1:
            mapped[k] = vs.pop()
            for sets in mapped.values():
                if isinstance(sets, set):
                    sets.discard(mapped[k])
    if len({*map(type, mapped.values())}) == 1:
        return dict(mapped)
    return isolate(mapped)
mapped = isolate(mapped)
for op, *ts in system:
    execute(state, *mapped[op], *ts)
print('Gold:', state[0])
