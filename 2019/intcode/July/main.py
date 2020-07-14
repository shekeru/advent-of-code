from assembler import *
from compiler import *
# Functions, Variables, Locals
# Declare Puts

# Declare Main
S_Mem = [
    "-global, 16, sbufR",
    "-global, 16, sbufN",
    "-global, 0, txt",
    b"Result: \0",
]
#Main += Puts.Call(["!txt"])

# Main.AddIf(Puts.Call(["!fizz"]))
# Generate Functions
from stdlib import div, mod, \
  puts, main, show
Script = [
    *div.Script,
    *mod.Script,
    *puts.Script,
    *show.Script,
    *main.Script,
]
Assembly = [*Pre, *S_Mem, *Script, *Post]
Pr = ProcessArray(Assembly)
with open("..\ins.txt", 'w') as F:
    F.write(Pr)
