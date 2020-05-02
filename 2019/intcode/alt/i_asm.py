def Generic(Code, *Args):
    Output = [Code]
    for Type, Value in Args:
        Output[0] = str(Type) + Output[0]
        Output.append(Value)
    Output[0] = int(Output[0])
    return Output

def Position(Value):
    return 0, Value

def Immediate(Value):
    return 1, Value

def Relative(Value):
    return 2, Value

ByteCode = {}
# Construct ByteCodes
def Add(A, B, C):
    return Generic('01', A, B, C)
ByteCode['ADD'] = Add

def Mul(A, B, C):
    return Generic('02', A, B, C)
ByteCode['MUL'] = Mul

def In(A):
    return Generic('03', A)
ByteCode['IN'] = In

def Out(A):
    return Generic('04', A)
ByteCode['OUT'] = Out

def JMP_True(A, B):
    return Generic('05', A, B)
ByteCode['1_JMP'] = JMP_True

def JMP_False(A, B):
    return Generic('06', A, B)
ByteCode['0_JMP'] = JMP_False

def LT(A, B, C):
    return Generic('07', A, B, C)
ByteCode['LT'] = LT

def EQ(A, B, C):
    return Generic('08', A, B, C)
ByteCode['EQ'] = EQ

def RBX(A):
    return Generic('09', A)
ByteCode['RBX'] = RBX

def Halt():
    return Generic('99')
ByteCode['HALT'] = Halt
