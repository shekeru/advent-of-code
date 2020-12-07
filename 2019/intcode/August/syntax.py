from lark import Lark

syntax = Lark(r"""
    start: _NL* stmnt*
    block: "{" _NL* stmnt* _NL* "}" _NL*
    function: "$def" fname "(" params ")" block
    params: symbol*
    fname: symbol
    set: "set!" symbol expr _NL
    term : expr+ _NL+
    stmnt: set| function | term
    expr: string | integer | symbol | "(" expr* ")" 
    symbol: /[a-zA-Z+=\-<>]+/
    integer: SIGNED_INT
    string: ESCAPED_STRING
    %import common.CNAME
    %import common.NEWLINE -> _NL
    %import common.SIGNED_INT
    %import common.ESCAPED_STRING
    %import common.WS_INLINE
    %ignore WS_INLINE
    COMMENT: "#" /[^\n]/*
    %ignore COMMENT
""", parser="earley")

def Parse(fname):
    return syntax.parse(
        open(f'code/{fname}.ic')
    .read())

from no_asm import *
def Build_AST(Node, Env = None):
    if Node.data == "start":
        Env = Program(OpCodes)
        for El in Node.children:
            if (V := Build_AST(El, Env)):
                Env.Body.append(V)
        return Env
    if Node.data == "stmnt":
        Child = Node.children[0]
        return Build_AST(Child, Env)
    if Node.data == "set":
        Name, Expr = Node.children
        Env[Build_AST(Name)] = Build_AST(Expr)
        return None
    if Node.data == "term":
        Op, *Args = map(Build_AST, Node.children)
        return Env.Find(Op)[Op](*Args)
    if Node.data == "expr":
        Value = [Build_AST(El, Env) for El in Node.children]
        return Value if len(Value) > 1 else Value[0]
    if Node.data == "symbol":
        Child = Node.children[0]
        return Symbol(Child.value)
    if Node.data == "integer":
        Child = Node.children[0]
        return int(Child.value)
    if Node.data == "string":
        Child = Node.children[0]
        return NewString(Child.value)
    print("AST:", Node.data)

pp = Parse('ex1')
print(pp.pretty())
Env = Build_AST(pp)
print(Env.Body, dict(Env))
print([*Env.Binary()])
