from collections import *

with open('ins.txt') as F:
    Original = defaultdict(int, {k: int(v) for
        k, v in enumerate(F.read().split(','))})

class VM:
    def __init__(s, Tape = Original):
        s.Tape = Tape.copy()
        s.Idx, s.Rbx = 0, 0
    def Step(s):
        Y, X, *s.Types = str(s.Tape[s.Idx]).rjust(5, '0')[::-1]
        print(VM.Ops[X+Y])
    def Resolve(s, Arg):
        if s.Types[Arg]:
    def Add(s):
        return 1
    def Mul(s):
        pass
    def Cin(s):
        pass
    def Cout(s):
        pass
    def Halt(s):
        pass
    Ops = {
        '01': Add,
        '02': Mul,
        '03': Cin,
        '04': Cout,
        '99': Halt
    }

a = VM()
a.Step()
