# Types
class Symbol(str):
    def __repr__(s):
        return f'Symbol({super().__str__()})'
    def __str__(s):
        return repr(s)

class Location:
    def __init__(s, code, name, value):
        s.pre, s.name = code, name
        s.value = value
    def __repr__(s):
        return f"{s.name}({s.value})"
    def Byte(s, Env):
        if isinstance(s.value, int):
            return s.value
        return Env.Find(s.value)

class AT(Location):
    def __init__(s, value):
        super().__init__(0, "AT", value)
    
class VAL(Location):
    def __init__(s, value):
        super().__init__(1, "VAL", value)

class REL(Location):
    def __init__(s, value):
        super().__init__(2, "REL", value)

Strings = {}
class String(AT):
    def __init__(s, value):
        s.ID = value
        super().__init__(s.ID)
        s.Bytes = (eval(value)+'\0').encode()
        Strings[s.ID] = s
    def Byte(s, Env):
        print(s.ID)
        return Env.Find(s.ID)[s.ID]
        
def NewString(value):
    if value in Strings:
        return Strings[value]
    return String(value)

# Structures
class Block(dict):
    def __init__(s, Parent):
        s.Parent = Parent
        s.Body = []
    def __repr__(s):
        return f"{s.Name}:{type(s)}"
    def Find(s, Var):
        if Var in s:
            return s
        if s.Parent != None:
            return s.Parent.Find(Var)        
        
class Program(Block):
    def __init__(s, Stdlib):
        super().__init__(None)
        s.update(Stdlib)
    def Binary(s, Env = None):
        Output = []
        for Item in s.Body:
            Output += Item.Binary(s)
        Output += [99]
        for Value, Obj in Strings.items():
            Obj.Idx = len(Output) - 1
            Output += Obj.Bytes
        for Idx, Loc in enumerate(Output):
            if isinstance(Loc, Location):
                Output[Idx] = Loc.Byte(s)
        return Output
            
class Function(Block):
    def __init__(s, Parent):
        super().__init__(Parent)
        
# Instructions
OpCodes = {}
class Instruction:
    def __init__(s, Code, *Args):
        s.Code, s.Args = Code, Args
    def Binary(s, Env):
        Output = [s.Code]
        for Value in s.Args:
            Ref = Env.Find(Value)[Value]
            Output[0] = str(Ref.pre) + Output[0]
            Output.append(Ref)
        Output[0] = int(Output[0])
        return Output
    
class OP_4(Instruction):
    def __init__(s, Loc):
        super().__init__('04', Loc)
        
OpCodes['putc'] = OP_4
