Tape = [[X, int(C)] for LN in
    open("2020/Day 08/input.txt")
for X, C in [LN.split()]]
# Simulation
def Eval():
    Acc = Ix = 0; Seen = set()
    while Ix < len(Tape):
        X, C = Tape[Ix]; Seen.add(Ix)
        if X == "jmp":
            Ix += C - 1
        elif X == "acc":
            Acc += C
        Ix += 1
        if Ix in Seen:
            return -Acc
    return Acc
# Correction
def Unhalt():
    for Ix, (X, C) in enumerate(Tape):
        T[0] = (T := Tape[Ix])[0].translate(str.maketrans
            ("jmno", "nojm")); yield Eval(); T[0] = X
# Results
print("Silver:", -Eval(), "\nGold:", next \
    (filter(lambda opt: opt > 0, Unhalt())))
