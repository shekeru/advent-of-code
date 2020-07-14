from compiler import Function
Mod = Function("mod", ["a", "b"], ["neg"])
# Declare Mod
Mod += ["mul, -1, >b, >neg"]
# Mod.AddLine("* -1 b neg")
Mod.AddLoop([
    "lt, >a, >b, $retn",
        "1_jmp, $retn, ~break",
    "add, >neg, >a, >a",
])
Mod += ["mul, 1, >a, $retn"]

Script = Mod.Generate()
