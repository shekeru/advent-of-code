import re, operator
# Operators
Forms = {
    '+': operator.add,
    '*': operator.mul,
}
# Tokenizer
def GetTokens(Ln):
    while Ln:
        for Ptn, Fn in [('\d+', int), ('.', str)]:
            V = re.match('(?:\s*)('+ Ptn +')(?:\s*)', Ln)
            if V:
                yield Fn(V.group(1))
                Ln = Ln[V.end():]
# Silver Models
def Silver(Line):
    return ExprS([*GetTokens(Line)])

def ExprS(Tokens):
    Value = Factor(Tokens, ExprS)
    while Tokens and Tokens[0] in Forms:
        Value = Forms[Tokens.pop(0)](Value, Factor(Tokens, ExprS))
    return Value

def Factor(Tokens, Function):
    if Tokens[0] != "(":
        return Tokens.pop(0)
    Tokens.pop(0)
    Value = Function(Tokens)
    Tokens.pop(0)
    return Value
# Gold Models
def Gold(Line):
    return ExprG([*GetTokens(Line)])

def ExprG(Tokens):
    Value = TermG(Tokens)
    while Tokens and Tokens[0] == "*":
        Value = Forms[Tokens.pop(0)](Value, TermG(Tokens))
    return Value

def TermG(Tokens):
    Value = Factor(Tokens, ExprG)
    while Tokens and Tokens[0] == "+":
        Value = Forms[Tokens.pop(0)](Value, Factor(Tokens, ExprG))
    return Value
# Results
Lines = [*open("Day 18/input.txt")]
print("Silver:", sum(map(Silver, Lines)))
print("Gold:", sum(map(Gold, Lines)))
