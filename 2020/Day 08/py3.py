Tape = [[X, int(C)] for LN in
    open("2020/Day 08/input.txt")
for X, C in [LN.split()]]
# Simulation
def Eval(First = True):
    Acc = Ix = 0; Seen = set()
    while Ix < len(Tape):
        X, C = T = Tape[Ix]; Seen.add(Ix)
        if First and "acc" != X:
            T[0] = {"jmp": "nop", "nop": "jmp"}[X]
            yield from Eval(False); T[0] = X
        Acc += C if "acc" == X else 0
        Ix += C if "jmp" == X else 1
        if Ix in Seen:
            Acc *= -1; break
    yield Acc
# Results
print("Silver:", -(V := [*Eval()])[-1],
    "\nGold:", next(x for x in V if x > 0))
