from re import compile
Graph = {M[1]: [(int(I), S) for I, S in Xs] for M, *Xs
    in map(compile(r'(^|\d\s)(\w+\s\w+)').findall,
open("2020/Day 07/input.txt"))}
# Silver Climbing
def Search(N):
    return {N} | {Z for K in Graph if
        N in (x[1] for x in Graph[K])
    for Z in Search(K)}
# Gold Traverse
def Total(N):
    return sum(I + Total(K) * I for I, K in Graph[N])
# Results
print("Silver:", len(Search("shiny gold"))
    - 1, "\nGold:", Total("shiny gold"))
