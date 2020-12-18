import re, operator
# How much cock could a cuckold cuck, if a cuckold could cuck cock?
Forms, Lines = {
    '+': operator.add,
    '*': operator.mul,
}, [*open("Day 18/input.txt")]
# Niggerlicious Lexer 6000000
def GetTokens(Ln):
    while Ln:
        for Ptn, Fn in [('\d+', int), ('[+*()]', str)]:
            if (V := re.match('(?:\s*)('+ Ptn +')(?:\s*)', Ln)):
                yield Fn(V.group(1)); Ln = Ln[V.end():]
# Part 1 Structure
class Silver(list):
    def Expr(Tokens):
        Value = Tokens.Factor()
        while Tokens and Tokens[0] in Forms:
            Value = Forms[Tokens.pop(0)](Value, Tokens.Factor())
        return Value
    def Factor(Tokens):
        if Tokens[0] != "(":
            return Tokens.pop(0)
        Tokens.pop(0)
        Value = Tokens.Expr()
        Tokens.pop(0)
        return Value
# Part 2 Structure
class Gold(Silver):
    def Expr(Tokens):
        Value = Tokens.Term()
        while Tokens and Tokens[0] == "*":
            Value = Forms[Tokens.pop(0)](Value, Tokens.Term())
        return Value
    def Term(Tokens):
        Value = Tokens.Factor()
        while Tokens and Tokens[0] == "+":
            Value = Forms[Tokens.pop(0)](Value, Tokens.Factor())
        return Value
# Results
Eval = lambda Ty: sum(Ty(GetTokens(X)).Expr() for X in Lines)
print("Silver:", Eval(Silver), "\nGold:", Eval(Gold))
