class Silver:
    def __init__(s, lines):
        s.lines = [*lines]
        s.vertical = [Column(xs) for xs in transpose(s.lines)]
    def __call__(s):
        x, y = map(lambda x: int("".join(x), 2),
            transpose([x.greeks for x in s.vertical]))
        return x * y

class Gold(Silver):
    def __init__(s, lines, mode, ix = 0):
        s.mode, s.ix = mode, ix
        super().__init__(lines)
    def __mul__(s, o):
        return int(s) * int(o)
    def __int__(s):
        if len(s.lines) == 1:
            return int(s.lines[0], 2)
        bit = s.vertical[s.ix].greeks[s.mode]
        lines = filter(lambda x: x[s.ix] == bit, s.lines)
        return int(Gold(lines, s.mode, s.ix + 1))

class Column(list):
    @property
    def greeks(s):
        return [b for _, b in sorted((s.count(x), x) for x in '01')]

def transpose(xss):
    return ["".join(xss[j][i] for j in range(len(xss))) for i in range(len(xss[0]))]

with open("i1.txt") as Fs:
    Xs = Fs.read().split()

print("Silver:", Silver(Xs)())
print("Gold:", Gold(Xs, 0) * Gold(Xs, 1))
