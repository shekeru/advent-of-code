from lexer import Open
Globals = {}

class Procedure:
    def __init__(s, Name, Args, Locals):
        s.Stack = ['rsp', *Args, *Locals][::-1]
        s.Name, s.Arity = Name, 1 + len(Args)
Open("ex1")
