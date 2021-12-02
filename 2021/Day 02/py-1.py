class Silver:
    def __call__(s, Act, Val):
        getattr(s, Act)(int(Val))
    def __init__(s):
        s.depth = 0
        s.position = 0
        s.aim = 0
    def __repr__(s):
        return str(s.depth * s.position)
    def forward(s, Val):
        s.depth += s.aim * Val
        s.position += Val
    def down(s, Val):
        s.depth += Val
    def up(s, Val):
        s.depth -= Val

class Gold(Silver):
    def down(s, Val):
        s.aim += Val
    def up(s, Val):
        s.aim -= Val

with open('i1.txt') as F:
    Parts = Silver(), Gold()
    for Ln in F:
        Y = Ln.split()
        for Fn in Parts:
            Fn(*Y)

for K in zip(('Silver:', 'Gold:'), Parts):
    print(*K)
