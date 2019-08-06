import operator, functools, collections
with open('2018/Day 21/input.txt') as f:
    ip, *tape = f.readlines()
r, codes, ip = "ABCDEF", {
    'add': '+',
    'mul': '*',
    'ban': '&',
    'bor': '|',
}, int(ip.split()[1])
# Day 21 Disassembler
def right(g, a, b, c):
    if c == b:
        return f"{r[c]} {g}= {r[a]}"
    if c == a:
        return f"{r[c]} {g}= {r[b]}"
    return f"{r[c]} = {r[a]} {g} {r[b]}"
def left(g, a, b, c):
    return f"{r[c]} {g}= {b}" if c == a \
        else f"{r[c]} = {r[a]} {g} {b}"
def assign(k, a, b, c):
    return f"{r[c]} = {r[a] if k == 'r' else a}"
def compare(g, kk, a, b, c):
    if kk == 'ir':
        return f"{r[c]} = {g}({a}, {r[b]})"
    if kk == 'ri':
        return f"{r[c]} = {g}({r[a]}, {b})"
    if kk == 'rr':
        return f"{r[c]} = {g}({r[a]}, {r[b]})"
def disassemble(xs):
    inst, *ys = xs.split()
    ys = map(int, ys)
    if inst[:-1] in codes:
        code = codes[inst[:-1]]
        if inst[-1] == 'r':
            return right(code, *ys)
        else:
            return left(code, *ys)
    if 'set' in inst:
        return assign(inst[-1], *ys)
    if 'gt' in inst:
        return compare('GT', inst[-2:], *ys)
    if 'eq' in inst:
        return compare('EQ', inst[-2:], *ys)
# Day 21 Decompiler
lines = [*map(disassemble, tape)]
updated = collections.defaultdict(str)
for i, ln in enumerate(lines):
    if f"{r[ip]} += 1" in ln:
        updated[i-1] = updated[i-1].replace('not ', '')
    elif f"{r[ip]} +=" in ln:
        updated[i] = f"  if not {lines[i-1][2]} do"
    elif f"{r[ip]} =" in ln:
        jmp = int(ln.split('= ')[-1])+1; updated[i] = f"{4*' '}goto label-{jmp}"
        updated[jmp] = f'label-{jmp}: {"{"+r[ip]}: {jmp-1}{"}"}\n' + updated[jmp]
    else:
        updated[i] += '  ' + ln
for k in sorted(updated):
    print(updated[k])
