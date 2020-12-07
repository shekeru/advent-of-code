Globals = {}

class Symbol(str):
    def __repr__(s):
        return f'Symbol({super().__str__()})'
    def __str__(s):
        return repr(s)

class Block(dict):
    def __init__(s, Parent):
        s.Parent = Parent
    def __repr__(s):
        return f"{s.Name}:{type(s)}"
    def Find(s, Var):
        if Var in s:
            return s
        if s.Parent != None:
            return s.Parent.Find(Var)
        
class Program(Block):
    def __init__(s, StdLib):
        super().__init__(None)
        s.update(StdLib)

class Function(Block):
    def __init__(s, Parent):
        super().__init__(Parent)
        s.Params = []

class While(Block):
    def __init__(s, Parent):
        super().__init__(Parent)

class Statement(Block):
    pass

from structs import *

def Build_AST(Node, Env = None):
    if Node.data == "start":
        Env = Program(Globals)
        Env.Body = [Build_AST(El, Env)
            for El in Node.children]
        return Env
    if Node.data == "function":
        Env = Function(Env)
        Name, Params, Body = Node.children
        Env.Name = Build_AST(Name, Env)
        Env.Params = Build_AST(Params, Env)
        Env.Body = Build_AST(Body, Env)
        Env.Parent[Env.Name] = Env
        return Env
    if Node.data == "while":
        Env = While(Env)
        Cond, Do = Node.children
        Env.Cond = Build_AST(Cond, Env)
        Env.Body = Build_AST(Do, Env)
        return Env
    if Node.data in ("fname"):
        El = Node.children[0]
        return Build_AST(El, Env)
    if Node.data in ("params", "block", "stmnt", "expr"):
        return [Build_AST(El, Env) for El in Node.children]
    if Node.data == "symbol":
        Child = Node.children[0]
        return Symbol(Child.value)
    if Node.data == "integer":
        Child = Node.children[0]
        return int(Child.value)
    print("AST:", Node.data)
    
