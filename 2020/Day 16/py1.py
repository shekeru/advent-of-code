import re, collections
Sum, Part1 = 0, collections.defaultdict(set)
Product, Part2 = 1, collections.defaultdict(set)
Ranges, Yours, Tickets = map(lambda x: x.split('\n'),
    open('Day 16/input.txt').read().split('\n\n'))
Valid = [[*map(int, Yours[1].split(','))]]
# Read Fields
for Field, *Line in map(re.compile('(?:^)[\w ]+|\d+.\d+').findall, Ranges):
    for Span in Line:
        A, B = map(int, Span.split('-'))
        Part1[Field] |= {*range(A, B+1)}
# Filter Tickets
for Line in Tickets[1:-1]:
    for Number in (Ln := [*map(int, Line.split(','))]):
        for Field in Part1:
            if Number in Part1[Field]:
                break
        else:
            Sum += Number; break
    else:
        Valid.append(Ln)
# Fields => Indexes
for Field in Part1:
    for I in range(len(Part1)):
        V = {T[I] for T in Valid}
        if not V - Part1[Field]:
            Part2[I].add(Field)
# Index => Field
while len(S := sorted(Part2, key = lambda k: len(Part2[k]))):
    Value = Part2[(Idx := S[0])].pop()
    if 'departure' in Value:
        Product *= Valid[0][Idx]
    for I in S[1:]:
        Part2[I].remove(Value)
    del Part2[Idx]
# Results
print("Silver:", Sum)
print("Gold:", Product)
