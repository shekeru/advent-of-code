Lines = [L.strip() for L in open("Day 19/input.txt")]
Ctx, Split = {}, Lines.index('')
Head, Body = Lines[:Split], Lines[1+ Split:]
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
# Match Strings
def Match(String):
    return int(max(Check(String, 0) | {0}) == len(String))
# Recursive Checks
def Check(String, Idx = 0):
    if isinstance(Ctx[Idx], str):
        return {1} if len(String) > 0 and String[0] == Ctx[Idx] else {}
    Seen = set()
    for Opts in Ctx[Idx]:
        Potential = {0}
        for Part in Opts:
            Potential = {Start + Delta for Start in Potential
                for Delta in Check(String[Start:], Part)}
        Seen |= Potential
    return Seen
# Results
print("Silver:", sum(map(Match, Body)))
Ctx[8] = [[42], [42, 8]]
Ctx[11] = [[42, 31], [42, 11, 31]]
print("Gold:", sum(map(Match, Body)))
