from generator import *
Compiler = {}
Current_Addr = 0
Globals = {}
LVars = {}

def Global(Bytes, Name):
    Globals[Name] = Current_Addr
    return ['0'] * int(Bytes)
Compiler['-GLOBAL'] = Global

def Vars(*Names):
    LVars.clear()
    for i, v in enumerate(Names):
        LVars[v] = i
    return []
Compiler['-VARS'] = Vars

def ProcessLine(Str):
    global Current_Addr
    Op, *Args = [x.strip() for x in Str.split(',')]
    if (Op := Op.upper()) in ByteCode:
        Bytes = ByteCode[Op](*map(Read, Args))
    else:
        Bytes = Compiler[Op](*Args)
    Current_Addr += len(Bytes); return Bytes

def ProcessArray(Lines):
    global Current_Addr; Program = []
    for Text in Lines:
        if isinstance(Text, str):
            Program += ProcessLine(Text)
        else:
            Current_Addr += len(Text)
            Program += Text
    for Idx, Byte in enumerate(Program):
        if isinstance(Byte, str):
            El = Byte[1:]
            if Byte[0] in "$!":
                Program[Idx] = Globals[El]
            if Byte[0] in "^":
                Program[Idx] = Idx + int(El)
    return ",".join(map(str, Program))

def Read(Arg):
    if '>' == Arg[0]:
        try:
            S = -int(Arg[1:])
        except:
            S = -LVars[Arg[1:]]
        return Relative(S)
    if '*' == Arg[0]:
        return Relative(Arg[1:])
    if '#' == Arg[0]:
        return Position(Arg[1:])
    if '$' == Arg[0]:
        return Position(Arg)
    return Immediate(Arg)

Pre, Halt = [
    "rbx, !halt",
    "mul, !halt, 1, *1",
    "0_jmp, 0, !main"
], [
    "-global, 0, halt", "halt"
]

S_Mem, Script = [
    "-global, 0, txt",
        b"shieeeet\0"
], [
    *Fn_Puts,
    # mod
    *Fn_Main
    # modcall?
]; Pr = ProcessArray([*Pre, *S_Mem, *Script, *Halt])
print(Pr)
