import re, collections
with open('input.txt') as f:
    parse = lambda x: map(int, re.findall(r'\d+', x))
    xs = map(parse, f.read().splitlines())
table = collections.defaultdict(int)
def apply(_, x ,y ,w, h):
    for i in range(y, y+h):
        for j in range(x, x+w):
            table[(i,j)] +=1
def match(lines):
    for (number, x, y, w, h) in lines:
        if sum(table[(i,j)] for i in range(y, y+h)
            for j in range(x, x+w)) == w*h:
                return number
[apply(*line) for line in xs]
overlap = sum([1 for v in table.values() if v > 1])
print('part 1:', overlap)
#print('part 2:', match(xs))
input()
