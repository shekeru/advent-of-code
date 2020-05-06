from i_asm import *; import re
Ln = re.compile(r"\{(.*?)\}|([^{\s}]+)")
Globals = {}
class Function:
    def __init__(s, Name, Args, Locals):
        s.Stack = ['rsp', *Args, *Locals][::-1]
        s.Name, s.Arity = Name, 1 + len(Args)
        s.Labels, s.Size = {}, len(s.Stack)
        s.Bytecode = [
            f"-alloc, 0, {s.Name}",
            RBX(Immediate(s.Size))
        ]; Globals[Name] = s
    def Generate(s):
        return s.Bytecode + [
            RBX(Immediate(-s.Size)),
            JMP_False(NIL, Relative(1)),
        ]
    def AddBody(s, Label, Data):
        if Label:
            s.Bytecode.append(f"-alloc, 0, {s.Name + Label}")
        s.Bytecode += [*map(s.Alt, Data)]
    def Assign(s, El):
        if El in s.Stack:
            return Relative(-s.Stack.index(El))
        if El in Globals:
            return Position(Globals[El])
        return Immediate(El)
    def Alt(s, Text):
        Op, *Arr = [x+y for x,y in Ln.findall(Text)]
        if Op in Globals:
            return Globals[Op].Call(Arr)
        if "+" == Op:
            return Add(*map(s.Assign, Arr))
        if ">>" == Op:
            return Out(*map(s.Assign, Arr))
        return Text
    def Call(s, Arr):
        V = 4 * s.Arity + 3 - 2
        O = [f"add, 0, $$ + {V}, *1"]
        for I, El in enumerate(Arr, 2):
            O.append(f"add, 0, {El}, *{I}")
        O.append()
        return O

Main = Function("main", [], [])
Puts = Function("puts", ["ptr"], ["ch"])
# Declare Puts
Puts.AddBody("_Loop", [
        "add, 0, >1, $$ + 2",
        "add, #1, 0, >0", # deref?
            "0_jmp, >0, !puts_Exit", #ret
        ">> ch",
        "+ 1 ptr ptr",
        "0_jmp, 0, !puts_Loop"
])
Puts.AddBody("_Exit", [])
Fn_Puts = Puts.Generate()
# Declare Main
Main.AddBody("", ["puts !txt"])
Fn_Main = Main.Generate()

Fn_Main
