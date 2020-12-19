Ctx, Lines = {}, [L.strip() for L in open("Day 19/input.txt")]
Head, Body = Lines[:(S := Lines.index(''))], Lines[1+S:]
# Header
for Ln in Head:
    Idx, *Term = Ln.split(': ')
    if "|" in Term[0]:
        Term = Term[0].split('|')
        Term = [[*map(int, R.split())] for R in Term]
    elif '"' not in Term[0]:
        Term[0] = [*map(int, Term[0].split())]
    else:
        Term = eval(Term[0])
    Ctx[int(Idx)] = Term
# Recursive Checks
def Check(String, Idx = 0, Fuck = ""):
    if isinstance(Ctx[Idx], str):
        return int(len(String) > 0 and String[0] == Ctx[Idx])
    for Opts in Ctx[Idx]:
        Offset = 0
        for Part in Opts:
            Consumed = Check(String[Offset:], Part, Fuck+"-")
            if not Consumed:
                break
            Offset += Consumed
        else:
            return Offset
    return 0
# Match Strings
def Match(String):
    return int(Check(String, 0) == len(String))
# Results
print("Silver:", sum(map(Match, Body)))
