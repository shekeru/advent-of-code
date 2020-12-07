from re import compile
Graph = {M[1]: [(int(I), S) for I, S in Xs] for M, *Xs
    in map(compile(r'(^|\d\s)(\w+\s\w+)').findall,
open("2020/Day 07/input.txt"))}
# Silver Climbing
def Construct(V):
    for K in Graph:
        if V in (x[1] for x in Graph[K]):
            yield from (K, *Construct(K))
# Gold Traverse
def Destruct(V):
    for I, K in Graph[V]:
        yield from (I, *(I * J for J in Destruct(K)))
# Results
print("Silver:", len({*Construct("shiny gold")}))
print("Gold:", sum(Destruct("shiny gold")))
