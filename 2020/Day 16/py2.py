from re import compile
Sum, Product, Fields = 0, 1, {}
Header, Yours, Tickets = map(lambda x: x.split('\n'),
    open('Day 16/input.txt').read().split('\n\n'))
Valid = [[*map(int, Yours[1].split(','))]]
# Read Fields
for Key, *Range in map(compile('(?:^)[\w ]+|\d+.\d+').findall, Header):
    Fields[Key] = lambda V, Range = [[*map(int, X.split('-'))]
        for X in Range]: any(1 for A, B in Range if A <= V <= B)
# Filter Tickets
for Line in Tickets[1:-1]:
    for Number in (Ln := [*map(int, Line.split(','))]):
        if not any(1 for K in Fields if Fields[K](Number)):
            Sum += Number; break
    else:
        Valid.append(Ln)
# Fields => Indexes
Graph = {I: {K for K in Fields if all(Fields[K] \
    (V[I]) for V in Valid)} for I in range(20)}
# Index => Field
while len(S := sorted(Graph, key = lambda k: len(Graph[k]))):
    Value = Graph[(Idx := S[0])].pop()
    [Graph[I].remove(Value) for I in S[1:]]
    if 'departure' in Value:
        Product *= Valid[0][Idx]
    del Graph[Idx]
# Results
print("Silver:", Sum)
print("Gold:", Product)
