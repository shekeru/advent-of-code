Graph = {Ch: Pr for Pr, Ch in
    (ln.strip().split(')') for ln
in open("2019/Day 06/input.txt"))}
# Iterate Backwards
def Flatten(x):
    while x in Graph:
        x = Graph[x]
        yield x
# Part 1
print("Silver:",
    sum(len((*Flatten(x),))
for x in Graph))
# Part 2
print("Gold:",
    len({*Flatten('SAN')}
^ {*Flatten('YOU')}))
