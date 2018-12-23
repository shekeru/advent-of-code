import operator, functools
with open('input.txt') as f:
    ip, *tape = f.readlines()
def compile(xs):
    inst, *ys = xs.split()
    return (*ops[inst], *map(int, ys))
def execute(xs, op, r1, r2, i, v, l):
    xs[l] = op(xs[i] if r1 else i, xs[v]
        if r2 else v); return xs
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
}; tape = [*map(compile, tape)]
def factors(n):
    return set(functools.reduce(list.__add__, ([i, n//i]
        for i in range(1, int(n**0.5)+1) if not n%i)))
def scan(i = 0):
    state = [i]+[0]*5
    while state[ip] < len(tape):
        inst = tape[state[ip]]
        if inst[0] == ops['eqrr'][0]:
            a,b,c = inst[-3:]
            return state[b if a is c else a]
        execute(state, *inst)
        state[ip] += 1
print('Silver:', sum(factors(scan(0))))
print('Gold:', sum(factors(scan(1))))
