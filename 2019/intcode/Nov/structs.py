class Program:
    def __init__(s):
        s.Tape = []
        s.Lines = []
        s.Labels = {}
    def __iadd__(s, op):
        s.Tape += op.GetBytes()
        s.Lines.append(op)
        return s
    def GetLabel(s, label):
        return s.Tape.index(s.Labels[label])
    def __repr__(s):
        return "\n".join(map(str, s.Lines))
    def Assembly(s):
        Output = []
        for Byte in s.Tape:
            Output.append(Byte.GetByte())
        return Output
class Binary:
    def SetLabel(s, name):
        Program.Labels[name] = s
# Operands
class Value(Binary):
    def __init__(s, code, val):
        s.code, s.value = code, val
    def __repr__(s):
        return f"{s.__class__.__name__}({s.value})"
    def GetByte(s):
        if isinstance(s.value, str):
            return Program.GetLabel(s.value)
        return s.value
# SubTypes
class AT(Value):
    def __init__(s, val):
        super().__init__(0, val)
class VAL(Value):
    def __init__(s, val):
        super().__init__(1, val)
class REL(Value):
    def __init__(s, val):
        super().__init__(2, val)
# Operators
class Operation(Binary):
    def __init__(s, code, *values):
        s.Bytes, s.OpCode = [*values], code
    def __repr__(s):
        return f"[{s.__class__.__name__}] {', '.join(map(str, s.Bytes))}"
    def GetByte(s):
        OutCode = s.OpCode
        for Byte in s.Bytes:
            OutCode = str(Byte.code) + OutCode
        return int(OutCode)
    def GetBytes(s):
        return [s, *s.Bytes]
# SubTypes
class Add(Operation):
    def __init__(s, *values):
        super().__init__('01', *values)
class Mul(Operation):
    def __init__(s, *values):
        super().__init__('02', *values)
class In(Operation):
    def __init__(s, *values):
        super().__init__('03', *values)
class Out(Operation):
    def __init__(s, *values):
        super().__init__('04', *values)
class Halt(Operation):
    def __init__(s, *values):
        super().__init__('99', *values)
# Start
def Build_AST(Expr):
    if Expr.name == "Number":
        return VAL(Expr.value)
    print(Expr)
Program = Program()
from lexer import Open
Tree = Open("ex1")
for Expr in Tree:
    Build_AST(Expr)
Program += Add(VAL(48), VAL('halt'), REL(1))
Program += Out(REL(1))
End = Halt()
End.SetLabel('halt')
Program += End
print(Program)
print(*Program.Assembly(), sep=",")
print(Program.GetLabel('halt'))
