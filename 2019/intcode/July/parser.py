from lexer import Open
from assembler import *

S_Mem = []
FnDict = {}

class Function:
    def __init__(s, Name, Args, Locals):
        s.Stack = ['rsp', *Args, *Locals][::-1]
        s.Name, s.Arity = Name, 1 + len(Args)
        s.Labels, s.Size = {}, len(s.Stack)
        s.Assembly, s.LoopCtr = [
            f"-global, 0, {s.Name}",
            f"-vars, " + ", ".join(s.Stack),
            f"rbx, {s.Size}"
        ], 0; FnDict[Name] = s
    def Call(s, Arr):
        V = 4 * s.Arity + 3 - 2
        O = [f"add, 0, !{V}, *1"]
        for I, El in enumerate(Arr, 2):
            O.append(f"add, 0, {El}, *{I}")
        O.append(f"0_jmp, 0, !{s.Name}")
        return O
    def End(s):
        return [f"rbx, {-s.Size}", "0_jmp, 0, *1"]
    def StartLoop(s):
        s.LoopCtr += 1
        return [f"-global, 0, {s.Name}_loop_{s.LoopCtr}"]
    def EndLoop(s, Array):
        return [f"0_jmp, 0, !{s.Name}_loop_{s.LoopCtr}",
        f"-global, 0, {s.Name}_break_{s.LoopCtr}"]
    def __iadd__(s, Data):
        s.Assembly += Data
        return s

def Resolve(Arg, Fn):
    if Arg.name in ("REF", "PTR"):
        return "%s_%s_%s" % (Arg.value[0],
            Fn.Name, Arg.value[1:])
    if Arg.name == "TERM":
        if Arg.value in Fn.Stack:
            return ">" + Arg.value
    return Arg.value

def Dispatch(Terms, Fn):
    Op, *Args = Terms
    if Op.name == "LOOP":
        Array = []
        Array += Fn.StartLoop()
        for Inner in Args:
            Array += Dispatch(Inner, Fn)
        Array = [x.replace("~break",
            f"!{Fn.Name}_break_{Fn.LoopCtr}") for x in Array]
        Array += Fn.EndLoop(Array)
        return Array
    if Op.name == "TERM":
        return FnDict[Op.value].Call \
            ([Resolve(x, Fn) for x in Args])
    return [", ".join([Op.name, *[Resolve \
        (x, Fn) for x in Args]])]

Array = Open("ex1")
for List in Array:
    Head = List[0]
    # Allocate Global Memory
    if Head.name == "BYTES":
        _, Term, Data = List
        Var, Val = Term.value, Data.value
        if Data.name == "STRING":
            S_Mem += ["-global, 0, %s" % Var,
                (eval(Val)+'\0').encode()]
        if Data.name == "NUMBER":
            S_Mem += ["-global, %s, %s" % (Val, Var)]
    # Allocate Function
    if Head.name == "DEFN":
        _, Term, Params, Locals, *Body = List
        Fn = Function(Term.value,
            [x.value for x in Params],
            [x.value for x in Locals])
        for Inner in Body:
            Fn += Dispatch(Inner, Fn)
        Fn += Fn.End()
        S_Mem += Fn.Assembly

S_Mem

Assembly = [*Pre, *S_Mem, *Post]
Pr = ProcessArray(Assembly)
with open("..\ins.txt", 'w') as F:
    F.write(Pr)

for Ln in Assembly:
    print(Ln)
