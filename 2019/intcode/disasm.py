from collections import defaultdict
OP = defaultdict(lambda: ("UNK!", 0), {
    1: ("ADD", 3),
    2: ("MUL", 3),
    3: ("IN", 1),
    4: ("OUT", 1),
    5: ("1, JMP", 2),
    6: ("0, JMP", 2),
    7: ("LT", 3),
    8: ("EQ", 3),
    9: ("RBX", 1),
    99: ("HALT", 0),
})
# File Input
with open('2019/intcode/ins.txt') as f:
    tape = [*map(int, f.read().split(','))]
# Read ASM
idx, rbx = 0, 0
while idx < len(tape):
    op_str = str(tape[idx]).rjust(5, '0')
    name, sz = OP[int(op_str[-2:])]
    mode = [*map(int, op_str[:-2][::-1])]
    pr = tape[idx + 1 : idx+sz+1]
    STR = "%s: %s -> " % (idx, name)
    for i in range(sz):
        if mode[i] == 1:
            STR += 'i(.%s, v = %s), ' % (idx+i+1, pr[i])
        elif mode[i] == 2:
            STR += '[rbx + %s], ' % i
        elif mode[i] == 0:
            STR += '{.%s, v = %s}, ' % (pr[i], tape[pr[i]] if pr[i] < len(tape) else '??')
    print(STR[:-2])
    idx += sz + 1
