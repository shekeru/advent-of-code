from compiler import Function
from stdlib.mod import Mod
Div = Function("div",
    ["a", "b"], ["neg", "i"])
# Declare Div
Div += [
    "mul, -1, >b, >neg",
    "mul, 0, 0, >i"
]

Div.AddLoop([
    "lt, >a, >b, $cmp",
        "1_jmp, $cmp, ~break",
    "add, >neg, >a, >a",
    "add, 1, >i, >i"
])

Div += [
    "mul, 1, >i, $retn"
]

Script = Div.Generate()
