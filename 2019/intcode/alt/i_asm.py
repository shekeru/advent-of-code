def Generic(Code, *Args):
    Output = [Code]
    for Type, Value in Args:
        Output[0] = str(Type) + Output[0]
        Output.append(Value)
    Output[0] = int(Output[0])
    return Output

def AT(Value):
    return 0, Value
REF = AT(0)

def VAL(Value):
    return 1, Value
NIL = VAL(0)

def REL(Value):
    return 2, Value

ByteCode = {}
# Construct ByteCodes
def Add(A, B, C):
    return Generic('01', A, B, C)
ByteCode['+'] = Add

def Mul(A, B, C):
    return Generic('02', A, B, C)
ByteCode['*'] = Mul

def In(A):
    return Generic('03', A)
ByteCode['<<'] = In

def Out(A):
    return Generic('04', A)
ByteCode['>>'] = Out

def JMP_True(A, B):
    return Generic('05', A, B)
ByteCode['1j'] = JMP_True

def JMP_False(A, B):
    return Generic('06', A, B)
ByteCode['0j'] = JMP_False

def LT(A, B, C):
    return Generic('07', A, B, C)
ByteCode['<'] = LT

def EQ(A, B, C):
    return Generic('08', A, B, C)
ByteCode['='] = EQ

def RBX(A):
    return Generic('09', A)

def Halt():
    return Generic('99')
