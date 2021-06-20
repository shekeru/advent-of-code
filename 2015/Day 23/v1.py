# Sheky Input
File = [x.strip() for x in open('2015/Day 23/ins.txt')]
# Proccess Input
Input = [Ln.replace(',', '').split() for Ln in File]
# Functions
class Computer:
    def __init__(s, Input, a = 0):
        s.State, s.Idx, s.Tape = {
            'a': a, 'b': 0,
        }, 0, Input
    def hlf(s, r):
        s.State[r] //= 2
    def tpl(s, r):
        s.State[r] *= 3
    def inc(s, r):
        s.State[r] += 1
    def jmp(s, o):
        s.Idx += int(o)
        return True
    def jie(s, r, o):
        if not s.State[r] & 1:
            s.Idx += int(o)
            return True
    def jio(s, r, o):
        if s.State[r] == 1:
            s.Idx += int(o)
            return True
    def Eval(s):
        while s.Idx < len(s.Tape):
            Op, *Args = s.Tape[s.Idx]
            if not getattr(s, Op)(*Args):
                s.Idx += 1
        return s.State['b']
# State
print("Silver:", Computer(Input).Eval())
print("Gold:", Computer(Input, 1).Eval())
