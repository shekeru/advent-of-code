from collections import defaultdict
from parse import Parse
from i_asm import *

class Function:
    def __init__(s, p, Args, Name, Locals):
        s.Program, s.Name = p, Name[0]
        s.Args, s.Locals = Args, Locals
        s.StackSize = 1 + len(Args) + len(Locals)
        p.Globals[s.Name], s.Location = s, p.Index
        s.Emplace()
    def Emplace(s):
        Insert = s.Program.PushTape
        Insert(RBX(VAL(s.StackSize)))
        Insert([
            *RBX(VAL(-s.StackSize)),
            *JMP_False(NIL, REL(1))
        ])

class Program:
    def __init__(s):
        s.Index, s.Tape, s.Globals = 0, [], {}
        s.PushTape(RBX(VAL('halt')))
        s.PushTape(JMP_False(NIL, VAL('main')))
    def PushTape(s, Bytes):
        s.Tape += Bytes
        s.Index += len(Bytes)
    def Terminate(s):
        s.Tape[1] = s.Index
        s.PushTape(Halt() + [s.Tape[1]])
p = Program()
Main = None
for Node in Parse('main').children:
    if Node.data == 'function':
        Function(p, *([Tk.value for Tk in Tr.children]
            for Tr in Node.children[:3]))
p.Terminate()
p.Tape
