from compiler import Function
from stdlib.mod import Mod
from stdlib.div import Div
Show = Function("show",
    ["int"], [])
# Declare Show
Show += [
    "add, 0, !sbufR, &r0",
    "add, 0, !sbufN, &r2"
]
Show.AddLoop([
    *Mod.Call([">int", 10]),
    "add, 48, $retn, ^r0",
    *Div.Call([">int", 10]),
    "add, 0, $retn, >int",
    "0_jmp, $retn, ~break",
    "add, 1, &r0, &r0",
])
Show += ["add, 0, &r0, &r1"]
Show.AddLoop([
    "add, ^r1, 0, ^r2",
    "eq, &r1, !sbufR, $cmp",
    "1_jmp, $cmp, ~break",
    "add, -1, &r1, &r1",
    "add, 1, &r2, &r2",
])
Show += ["add, 0, !sbufN, $retn"]

Script = Show.Generate()
