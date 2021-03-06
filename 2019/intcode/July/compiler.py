from i_asm import *; import re
Ln = re.compile(r"\{(.*?)\}|([^{\s}]+)")

class Function:
    def __init__(s, Name, Args, Locals):
        s.Stack = ['rsp', *Args, *Locals][::-1]
        s.Name, s.Arity = Name, 1 + len(Args)
        s.Labels, s.Size = {}, len(s.Stack)
        s.Assembly = [
            f"-global, 0, {s.Name}",
            f"-vars, " + ", ".join(s.Stack),
            f"rbx, {s.Size}"
        ]; s.LoopCtr = 0
    def Generate(s):
        return s.Assembly + [
            f"rbx, {-s.Size}",
            "0_jmp, 0, *1"]
    def AddLoop(s, Data):
        s.LoopCtr += 1; s.Assembly += [
          f"-global, 0, {s.Name}_loop_{s.LoopCtr}",
          *map(lambda x: x.replace("~break",
            f"!{s.Name}_break_{s.LoopCtr}"), Data),
          f"0_jmp, 0, !{s.Name}_loop_{s.LoopCtr}",
          f"-global, 0, {s.Name}_break_{s.LoopCtr}"]
    def JumpIf(s, Data):
        s.LoopCtr += 1; return [
            f"1_jmp, $cmp, !{s.Name}_cond_{s.LoopCtr}",
        *Data, f"-global, 0, {s.Name}_cond_{s.LoopCtr}",]
    def Call(s, Arr):
        V = 4 * s.Arity + 3 - 2
        O = [f"add, 0, !{V}, *1"]
        for I, El in enumerate(Arr, 2):
            O.append(f"add, 0, {El}, *{I}")
        O.append(f"0_jmp, 0, !{s.Name}")
        return O
    def __iadd__(s, Data):
        s.Assembly += Data
        return s
