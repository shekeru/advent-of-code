from i_asm import *; import re
Ln = re.compile(r"\{(.*?)\}|([^{\s}]+)")
Globals = {}

class Function:
    def __init__(s, Name, Args, Locals):
        s.Stack = ['rsp', *Args, *Locals][::-1]
        s.Name, s.Arity = Name, 1 + len(Args)
        s.Labels, s.Size = {}, len(s.Stack)
        s.Bytecode = [
            f"-global, 0, {s.Name}",
            f"-vars, " + ", ".join(s.Stack),
            f"rbx, {s.Size}"
        ]; Globals[Name] = s
        s.LoopCtr = 0
    def Generate(s):
        Flatten = []
        for item in s.Bytecode.copy():
            if isinstance(item, list):
                Flatten += item
            else:
                Flatten += [item]
        return Flatten + [
            f"rbx, {-s.Size}",
            "0_jmp, 0, *1"
        ]
    def AddBody(s, Label, Data):
        if Label:
            s.Bytecode.append(f"-global, 0, {s.Name + Label}")
        s.Bytecode += [*map(s.Alt, Data)]
    def AddLoop(s, Data):
        s.LoopCtr += 1; s.Bytecode += [
          f"-global, 0, {s.Name}_loop_{s.LoopCtr}",
          *map(lambda x: x.replace("~break",
            f"!{s.Name}_break_{s.LoopCtr}"), Data),
          f"0_jmp, 0, !{s.Name}_loop_{s.LoopCtr}",
          f"-global, 0, {s.Name}_break_{s.LoopCtr}"]
    def Alt(s, Text):
        Op, *Arr = [x+y for x,y in Ln.findall(Text)]
        if Op in Globals:
            return Globals[Op].Call(Arr)
        return Text
    def Call(s, Arr):
        V = 4 * s.Arity + 3 - 2
        O = [f"add, 0, ^{V}, *1"]
        for I, El in enumerate(Arr, 2):
            O.append(f"add, 0, {El}, *{I}")
        O.append(f"0_jmp, 0, !{s.Name}")
        return O
    def __iadd__(s, Data):
        s.Bytecode += Data
        return s
# Functions, Variables, Locals
Main = Function("main", [], [])
Puts = Function("puts", ["ptr"], ["ch"])
# Declare Puts
Puts.AddLoop([
        "add, 0, >ptr, ^2",
        "add, #1, 0, >ch", # deref?
            "0_jmp, >ch, ~break", #ret
        "cout, >ch",
        "add, 1, >ptr, >ptr",
])
# Declare Main
Main += Puts.Call(["!txt"])
# Generate Functions
Fn_Puts = Puts.Generate()
Fn_Main = Main.Generate()
