def op(code, x = 0, y = 0, z = 0):
    im = "".join(map(str, [z, y, x]))
    return int(im.lstrip('0') + '0' + str(code))
# Instructions Section
iDict, Ix, iM, rX = {
    "halt": '99',
    "rbx": '9',
    "eq": '8',
    "lt": '7',
    "jmp,0": '6',
    "jmp,1": '5',
    "out": '4',
    "cin": '3',
    "mul": '2',
    "add": '1',
}, 0, 1, 2
# Code Construction
def code(st, x = 0, y = 0, z = 0):
    im = "".join(map(str, [z, y, x]))
    op = im.lstrip('0') + '0' + iDict[st]
    def parser(*xs):
        return [int(op)]+[x.idx if isinstance(x,
            Function) else x for x in xs]
    return parser
# Impl Function
class Function:
    def __init__(f, s, n):
        f.s, f.args = s, [*range(n + 1)]
    def call(f, xs):
        if isinstance(xs[0], str):
            xs[0] = f.s.get_idx() + 4 * len(xs) + 3
        for i, x in enumerate(xs):
            f.s.tape += code('add', iM, iM, rX)(x, 0, i)
        f.s.tape += code('jmp,0', iM, iM)(0, f.idx)
    def add(f, xs):
        locals = set()
        f.idx = f.s.get_idx()
        for i, x in enumerate(xs):
            if isinstance(x, str):
                if x[0] == '$':
                    xs[i] = f.idx + xs.index(x[1:])
                elif x[0] == "+":
                    xs[i] = f.idx + int(x[1:])
                else:
                    locals.add(i)
        for i in locals:
            xs[i] = 0
        f.s.tape += xs
        return f.idx
# Main Compiler
class Assembly:
    def __init__(s):
        s.tape = [
            *code('rbx', iM)('rbx'),
            *code('jmp,0', iM, iM)(0, 'mdx'),
            *code('halt')(-1),
        ]; s.retn = len(s.tape) - 1
        s.exit =  s.retn - 1
    def get_idx(s):
        return len(s.tape)
    def output(s):
        rbx = asm.tape.index("rbx")
        s.tape[rbx] = len(s.tape)
        return ",".join(map(str, s.tape))
    def emplace(s, data, term = 0):
        value = s.get_idx()
        s.tape += [*map(ord, data)]
        s.tape.append(term)
        return value
    def var(s, value):
        where = s.get_idx()
        s.tape.append(value)
        return where
# Implementation
    def impl_add(s):
        fn = Function(s, 2)
        jmp, a, b = fn.args
        fn.add([
            *code('add', rX, rX, Ix)(a, b, s.retn),
            *code('jmp,0', iM, rX)(0, jmp),
        ]); return fn.idx
    def impl_sub(s):
        fn = Function(s, 2)
        jmp, a, b = fn.args
        fn.add([
            *code('mul', iM, rX, Ix)(-1, b, '$nb'),
            *code('add', iM, rX, Ix)('nb', a, s.retn),
            *code('jmp,0', iM, rX)(0, jmp),
        ]); return fn.idx
    def impl_div(s):
        idx = s.get_idx()
        jmp, a, b = range(3)
        s.tape += [
            op(1, 1, 1), 0, 0, s.retn,
            op(2, 1, 2), -1, b, idx+9,
            # loop?
            op(1, 1, 2, 2), 0, a, a,
            op(7, 2, 2), b, a, idx+17,
            op(6, 1, 2), 0, jmp,
            op(1), idx+17, s.retn, s.retn,
            *code("jmp,1", iM, iM)(1, idx+8),
        ]; return idx
    def impl_mul(s):
        idx = s.get_idx()
        jmp, a, b = range(3)
        s.tape += [
            op(2, 2, 2, 0), a, b, s.retn,
            op(6, 1, 2), 0, jmp,
        ]; return idx
    def impl_print(s):
        fn = Function(s, 1)
        jmp, xs = fn.args
        fn.add([
            op(1, 1, 2), 0, xs, "$ptr",
            op(1, 0, 1, 0), "ptr", 0, "$chr",
            op(6, 0, 2), "$chr", jmp, #exit
            *code("out", iM)("chr"), #putc
            op(1, 1, 0), 1, "$ptr", "$ptr", #load char
            *code("jmp,1", iM, iM)(1, "+4"), # loop
        ]); return fn
# Insert Function Call
    def call_fn(s, addr, *xs):
        xs = list(xs)
        if isinstance(xs[0], str):
            xs[0] = s.get_idx() + 4 * len(xs) + 3
        for i, x in enumerate(xs):
            s.tape += code('add', iM, iM, rX)(x, 0, i)
        s.tape += code('jmp,0', iM, iM)(0, addr)
# Fuck It
asm = Assembly()
env, vars, text = {
    'puts': asm.impl_print(),
    #'div': asm.impl_div(),
    #'sub': asm.impl_sub(),
    #'mul': asm.impl_mul(),
    #'add': asm.impl_add(),
}, {
    # 'A': asm.var(77),
    # 'B': asm.var(11),
}, {
    1: asm.emplace("sup\n"),
    2: asm.emplace("niggy\n"),
} # Main Proc?
main = asm.tape.index("mdx")
asm.tape[main] = asm.get_idx()
# User Space
#asm.call_fn(env['div'], "", vars['A'], vars['B'])
env['puts'].call(["", text[1]])
env['puts'].call(["", text[2]])
# asm.call_fn(env['puts'], "", text['world']),
# More Assembly
asm.tape += [
    # JMP Exit
    #*code('out', Ix)(asm.retn),
    *code('jmp,0', iM, iM)(0, asm.exit),
]; print(asm.output())
