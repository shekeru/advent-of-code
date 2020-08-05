from i_asm import *
# Variables
Program = []
Compiler = {}
Current_Addr = 0
Globals = {}
LVars = {}
# Assembler Flags
def Global(Bytes, Name):
    Globals[Name] = Current_Addr
    return [0] * int(Bytes)
Compiler['-GLOBAL'] = Global

def Vars(*Names):
    LVars.clear()
    for i, v in enumerate(Names):
        LVars[v] = i
    return []
Compiler['-VARS'] = Vars
# Assembler
def ProcessArray(Lines):
    global Current_Addr, Program
    for Text in Lines:
        if isinstance(Text, str):
            Output = ProcessLine(Text)
            print(Current_Addr, Output, Text)
            Program += Output
        else:
            Current_Addr += len(Text)
            Program += Text
    for Idx, Byte in enumerate(Program):
        if isinstance(Byte, str):
            if Byte in Globals:
                Program[Idx] = Globals[Byte]
            elif Byte[0] == "^":
                Globals['&'+Byte[1:]] = Idx
                Program[Idx] = 0
            elif Byte[0] != "&":
                Program[Idx] = Idx + int(Byte)
    for Idx, Byte in enumerate(Program):
        if isinstance(Byte, str):
            if Byte in Globals:
                Program[Idx] = Globals[Byte]
    return ",".join(map(str, Program))

def ProcessLine(Str):
    global Current_Addr
    Op, *Args = [x.strip() for x in Str.split(',')]
    if (Op := Op.upper()) in ByteCode:
        Bytes = ByteCode[Op](*map(Read, Args))
    else:
        Bytes = Compiler[Op](*Args)
    Current_Addr += len(Bytes); return Bytes

def Read(Arg):
    Sign, *Body = Arg
    Body = "".join(Body)
    if '>' == Arg[0]:
        try: # indexed from stack
            S = -int(Arg[1:])
        except: # by text
            S = -LVars[Arg[1:]]
        return Relative(S)
    if Sign == '*': # add to stack
        return Relative(int(Body))
    if Sign == '!': # 0j, !main
        return Immediate(Body)
    if Sign == '$': # $retn
        return Position(Body)
    if Sign in "^&":
        return Position(Arg)
    return Immediate(int(Arg))
# Utility Shit
Pre, Post = [
    "rbx, !_halt",
    "mul, !_halt, 1, *1",
    "0_jmp, 0, !main",
], [
    "-global, 1, _rx1",
    "-global, 0, _halt",
"halt"]
