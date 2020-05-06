from collections import defaultdict
from parse import Parse
from i_asm import *

class Statement:
    def __init__(s, fn, Op, *args):
        s.Function, s.Op = fn, Op.children[0]
        s.Location = s.Function.Program.Index
        B_Args, s.Inc = [s.AddArg(*xs) for xs
            in enumerate(args, 1)], 1
        s.Push = s.Function.Program.PushTape
        if s.Op in ByteCode:
            s.Push(ByteCode[s.Op](*B_Args))
            return
        if s.Op in s.Function.Program.Globals:
            Fn = s.Function.Program.Globals[s.Op]
            s.CallFn(VAL(len(Fn.Args) * 4 + s.Location + 3))
            for Arg in B_Args:
                s.CallFn(Arg)
            s.Push(JMP_False(NIL, VAL(s.Op)))
            return
        print('stmt error:', s.Op)
    def CallFn(s, X):
        s.Push(Add(NIL, X, REL(s.Inc))); s.Inc += 1
    def AddArg(s, I, A):
        V = A.children[0].value
        Stack = s.Function.Stack
        if A.data == 'string':
            V = eval(V)
            s.Function.Program.StaticMem.append \
                ((hash(V), (V + '\0').encode()))
            return VAL(hash(V))
        if A.data == 'literal':
            return VAL(int(V))
        if A.data == 'mem_slot':
            s.Function.Labels[V] = s.Function \
                .Program.Index + I; return REF
        if A.data == 'mem_ref':
            return AT(V)
        if A.data == 'ctrl_ref':
            return VAL(V)
        if A.data == 'term':
            if V in Stack:
                V = -Stack.index(V)
                return REL(V)
        print('arg:', A)

class Function:
    def __init__(s, p, Args, Name, Locals):
        s.Program, s.Name = p, Name[0]
        s.Args, s.Locals = ['rsp', *Args], Locals
        s.Stack, s.Labels = [*s.Args, *Locals], {}
        s.Stack, s.Size = s.Stack[::-1], len(s.Stack)
        p.Globals[s.Name], s.Location = s, p.Index
    def Emplace(s, Stmts):
        Insert = (Pr := s.Program).PushTape
        Insert(RBX(VAL(s.Size)))
        # Statements
        for St in Stmts:
            if St.data == 'asm_line':
                Statement(s, *St.children)
                continue
            if St.data == 'ctrl_label':
                s.Labels[St.children[0]. \
                    value] = s.Program.Index
                continue
            print(St)
        # Second pass
        for Ix in range(s.Location, s.Program.Index):
            if (Name := s.Program.Tape[Ix]) in s.Labels:
                s.Program.Tape[Ix] = s.Labels[Name]
                #print(Name, Ix, '->', s.Labels[Name])
        # Post
        Insert([
            *RBX(VAL(-s.Size)),
            *JMP_False(NIL, REL(1))
        ])

class Program:
    def __init__(s):
        s.Index, s.Tape, s.Globals = 0, [], {}
        s.PushTape(RBX(VAL('halt')))
        s.PushTape(Mul(VAL(1), AT(1), REL(1)))
        s.PushTape(JMP_False(NIL, VAL('main')))
        s.StaticMem = []
    def PushTape(s, Bytes):
        s.Tape += Bytes
        s.Index += len(Bytes)
    def Finish(s):
        for key, val in s.StaticMem:
            s.Globals[key] = Static(s.Index)
            s.PushTape(val)
        s.Tape[1] = s.Index
        s.PushTape(Halt())
        for Ix, Byte in enumerate(s.Tape):
            if Byte in s.Globals:
                s.Tape[Ix] = s.Globals[Byte].Location
        print(Str := ",".join(map(str, s.Tape)))
        open('../ins.txt', 'w').write(Str)

class Static:
    def __init__(s, Idx):
        s.Location = Idx

p = Program()
Main = None
for Node in Parse('test_3').children:
    if Node.data == 'function':
        Meta, Stmts = Node.children[:3], Node.children[3:]
        Function(p, *([Tk.value for Tk in Tr.children]
            for Tr in Meta)).Emplace(Stmts)
p.Finish()
