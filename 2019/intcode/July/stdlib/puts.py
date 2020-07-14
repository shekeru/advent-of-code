from compiler import Function
Puts = Function("puts", ["ptr"], ["ch"])

Puts += ["add, 0, >ptr, &puts_ref"]

Puts.AddLoop([
    "add, ^puts_ref, 0, >ch", # deref?
        "0_jmp, >ch, ~break", #ret
    "cout, >ch",
    "add, 1, &puts_ref, &puts_ref",
])

Script = Puts.Generate()
