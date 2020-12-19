Match = lambda Str: int(max([*Check(Str, 0), 0]) == len(Str))
Ctx, Lines = {}, [L.strip() for L in open("Day 19/input.txt")]
Header, Body = Lines[:(S := Lines.index(''))], Lines[1+ S:]
# Giving Head is Fun
for Ln in Header:
    Idx, *Term = Ln.split(': ')
    if "|" in Term[0]:
        Term = Term[0].split('|')
        Term = [[*map(int, R.split())] for R in Term]
    elif '"' not in Term[0]:
        Term[0] = [*map(int, Term[0].split())]
    else:
        Term = eval(Term[0])
    Ctx[int(Idx)] = Term
# Recursive Chad Function
def Check(String, Idx = 0):
    if isinstance(Ctx[Idx], str):
        yield from [1] if len(String) > 0 and \
            String[0] == Ctx[Idx] else []; return
    for Opts in Ctx[Idx]:
        Potential = [0]
        for Part in Opts:
            Potential = [Start + Delta for Start in Potential
                for Delta in Check(String[Start:], Part)]
        yield from Potential
# Do The Needful Sir
print("Silver:", sum(map(Match, Body)))
Ctx.update({8: [[42], [42, 8]], 11: [[42, 31], [42, 11, 31]]})
print("Gold:", sum(map(Match, Body)))
