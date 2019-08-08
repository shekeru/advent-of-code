import operator, functools, math
with open('2018/Day 21/input.txt') as f:
    ip, *feed = f.readlines()
def compile(xs):
    inst, *ys = xs.split()
    return (*ops[inst], *map(int, ys))
def execute(xs, op, r1, r2, i, v, l):
    xs[l] = int(op(xs[i] if r1 else i, xs[v]
        if r2 else v)); return xs
ip, ops = int(ip.split()[1]), {
    'addr': (operator.add, True, True), # addr
    'addi': (operator.add, True, False), # addi
    'mulr': (operator.mul, True, True), # mulr
    'muli': (operator.mul, True, False), # muli
    'banr': (operator.and_, True, True), #banr
    'bani': (operator.and_, True, False), # bani
    'borr': (operator.or_, True, True), #borr
    'bori': (operator.or_, True, False), # bori
    'setr': (lambda a,b: a, True, None), # setr
    'seti': (lambda a,b: a, False, None), # seti
    'gtir': (operator.gt, False, True), # gtir
    'gtri': (operator.gt, True, False), # gtri
    'gtrr': (operator.gt, True, True), # gtrr
    'eqir': (operator.eq, False, True), # eqir
    'eqri': (operator.eq, True, False), # eqri
    'eqrr': (operator.eq, True, True), # eqrr
}; tape = [*map(compile, feed)]
def scan_vm(gold = False):
    ticks, state, seen = 0, [0]*6, []
    while state[ip] < len(tape):
        inst = tape[state[ip]]
        if inst[:3] == ops['eqrr']:
            value = state[inst[-3]]
            if not gold:
                return value
            if value not in seen:
                seen.append(value)
            else:
                return seen[-1]
        if inst[:3] == ops['gtrr']:
            state[1] = math.ceil((state[5] + 1) / 256)
            state[2] = state[1] - 1
            state[5] = state[2]
            state[1] *= 256
        execute(state, *inst)
        state[ip] += 1; ticks += 1
print('Silver:', scan_vm())
print('Gold:', scan_vm(True))
