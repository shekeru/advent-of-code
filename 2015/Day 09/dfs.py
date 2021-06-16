import re, copy
# Read File
Opts, Graph, Match = set(), {}, re.compile(r'(\w+)\sto\s(\w+)\D+(\d+)')
for *Pairs, Dist in Match.findall(open('2015/Day 09/ins.txt').read()):
    Graph[tuple(sorted(Pairs))] = int(Dist); Opts |= {*Pairs}
# Helper Structure
class Location:
    def __init__(s, Start):
        s.Where, s.Dist = [Start], 0
        s.Left = Opts - {Start}
    def __repr__(s):
        return f"{', '.join(s.Where)} = {s.Dist}"
    def Advance(s):
        for Next in s.Left:
            (Alt := copy.deepcopy(s)).Where.append(Next)
            Alt.Dist += Graph[(*sorted(Alt.Where[-2:]), )]
            Alt.Left.remove(Next); Alt.Advance()
        if not s.Left:
            Location.Min = min(Location.Min, s.Dist)
            Location.Max = max(Location.Max, s.Dist)
    Min, Max = sum(Graph.values()), 0
for Start in Opts:
    Location(Start).Advance()
# Display Output
print("silver:", Location.Min)
print("gold:", Location.Max)
