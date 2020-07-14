from compiler import Function
from stdlib.show import Show
from stdlib.puts import Puts
from stdlib.mod import Mod
Main = Function("main", [],
    ["i", "sum"])

Main += [
    "mul, 0, 0, >i",
    "mul, 0, 0, >sum"
    ]
Main.AddLoop([
    # increment to 1000
    "add, 1, >i, >i",
    "lt, >i, 10, $cmp",
    "0_jmp, $cmp, ~break",
    # If either is zero, will zero
    *Mod.Call([">i", "3"]),
    "add, 0, $retn, $cmp",
    *Mod.Call([">i", "5"]),
    "mul, $cmp, $retn, $cmp",
    *Main.JumpIf([
        "add, >i, >sum, >sum",
    ]),
])

Main += [
    *Puts.Call(["!txt"]),
    *Show.Call([">sum"]),
    *Puts.Call(["$retn"]),
]

Script = Main.Generate()
