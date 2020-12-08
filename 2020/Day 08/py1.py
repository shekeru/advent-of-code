Input = [[X, int(C)] for LN in
    open("2020/Day 08/input.txt")
for X, C in [LN.split()]]
# Simulation
def Eval(Tape):
    Acc = Ix = 0; Seen = set()
    while Ix < len(Tape):
        if Ix in Seen:
            return Acc, False
        X, C = Tape[Ix]; Seen.add(Ix)
        if X == "jmp":
            Ix += C - 1
        elif X == "acc":
            Acc += C
        Ix += 1
    return Acc, True
# Correction
def Unhalt(Tape):
    for Ix, (X, C) in enumerate(Tape):
        if X == "nop" and C:
            Tape[Ix][0] = "jmp"
        elif X == "jmp":
            Tape[Ix][0] = "nop"
        else:
            continue
        yield Eval(Tape)
        Tape[Ix][0] = X
# Results
print("Silver:", Eval(Input)[0])
print("Gold:", next(filter(lambda opt:
    opt[1], Unhalt(Input)))[0])
