def op(code, x = 0, y = 0, z = 0):
    im = "".join(map(str, [z, y, x]))
    return im.lstrip('0') + '0' + str(code)
class Assembly:
    def __init__(s):
        s.proc = [op(9, 1), 'rbx',
            op(6, 1, 1), 0, 'mdx', 99]
        s.exit = len(s.proc) - 1
    def output(s):
        s.proc[1] = len(s.proc)
        return ",".join(map(str, s.proc))
    def emplace(s, data):
        value = s.get_idx()
        s.proc += data + [0]
        return value
# Implementation
    def impl_add(s):
        idx = asm.get_idx()
        r, a, b, c = [1,2,3,4][::-1]
        s.proc += [
            op(1, 2, 2, 2), -a, -b, -c,
            # retn
            op(9, 1), -4,
            op(6, 1, 2), 0, -r,
        ]; return idx
    def impl_print(s):
        idx = asm.get_idx()
        ret, xs = range(2)
        s.proc += [
            op(1, 1, 2), 0, xs, idx + 5,
            op(1, 0, 1, 0), 0, 0, idx+12,
            op(6, 0, 2), idx+12, ret,
            op(4, 1), 0,
            op(1, 1, 0), 1, idx + 5, idx+5,
            op(5, 1, 1), 1, idx+4,
        ]; return idx
    def get_idx(s):
        return len(s.proc)
# Fuck It
asm = Assembly()
env = {
    'puts': asm.impl_print(),
    'hello': asm.emplace([*map(ord, "hello")]),
    #'add': asm.impl_add(),
}; asm.proc[4] = asm.get_idx()
# Main Proc?
asm.proc += [
    op(1, 1, 1, 2), asm.exit, 0, 0,
    op(1, 1, 1, 2), env['hello'], 0, 1,
    op(6, 1, 1), 0, env['puts'],
    op(6, 1, 1), 0, asm.exit,
]
print(asm.output())
