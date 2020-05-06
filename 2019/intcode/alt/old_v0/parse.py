from i_asm import *
from gen import *
Current_Addr = 0
Labels = {}

Compiler = {}
def Alloc(Bytes, Name):
    Labels[Name] = Current_Addr
    return ['0'] * int(Bytes)
Compiler['-ALLOC'] = Alloc

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
            if Byte[0] in "$!":
                El, *L = Byte[1:].split('+')
                Program[Idx] = Idx if (El := El
                    .strip()) == "$" else Labels[El]
                if L:
                    Program[Idx] += int(L[0])
    return ",".join(map(str, Program))

def Read(Arg):
    if '>' == Arg[0]:
        S = -int(Arg[1:])
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
    "0_jmp, 0, !main"
], [
    "-alloc, 0, halt", "halt"
]

S_Mem, Script = [
    "-alloc, 1, retn",
    "-alloc, 3, idk",
    "-alloc, 0, txt",
        b"shieeeet\0"
], [
    *Fn_Puts,
    # mod
    "-alloc, 0, mod",
        "mul, -1, >2, *1",
        "lt, >1, >2, *2",
            "1_jmp, *2, >0",
        "add, *1, >1, >1",
    "0_jmp, 0, !mod + 4",
    # mod 2
    "-alloc, 0, mod2",
        "mul, -1, >2, *1",
        "-alloc, 0, start_mod",
        "lt, >1, >2, *2",
            "1_jmp, *2, !exit_mod",
        "add, *1, >1, >1",
        "0_jmp, 0, !start_mod",
    "-alloc, 0, exit_mod",
    "add, 0, >1, $retn",
    "0_jmp, 0, >0",
    # N_times
    "-alloc, 0, loop_for", #2
        "add, 48, >1, *1",
        "out, *1", "out, 10",
        "add, >1, >3, >1",
        "lt, >1, >2, *2",
        "1_jmp, *2, !loop_for",
    "0_jmp, 0, >0",
    # Main Entry
    "-alloc, 0, main",
    "rbx, 1",
    # 19 % 5
    # "rbx, 3",
    #     "add, 0, !retC, >0",
    #     "add, 0, 12, >1",
    #     "add, 0, 5, >2",
    #     "0_jmp, 0, !mod2",
    #     "-alloc, 0, retC",
    # "rbx, -3",
    # "add, 0, $retn, $idk",
    # # rsp on stack
    # "rbx, 4",
    #     "add, 0, !retA, >0",
    #     "add, 0, 0, >1",
    #     "add, 0, $idk, >2",
    #     "add, 0, 1, >3",
    #     "0_jmp, 0, !loop_for",
    #     "-alloc, 0, retA",
    # "rbx, -4",
    # next call
        "add, 0, !retB, *1",
        "add, 0, !txt, *2",
        "0_jmp, 0, !puts",
        "-alloc, 0, retB",
    "rbx, -1",
    # modcall?
]; Pr = ProcessArray([*Pre, *S_Mem, *Script, *Halt])
print(Pr)
