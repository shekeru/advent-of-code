Lines = [[{k: v - 3 if v > 3 else v 
    for v, k in enumerate("ABCXYZ", 1)}[x] for x in ln.split()] 
    for ln in open('2022/Day 02/input.txt')]

def Silver(f, g):
    return g + {
        f+1: 6, f-2: 6, f: 3,
    }.get(g, 0)


def Gold(f, g):
    return 3 * (g - 1) + {
        3: f+1 if f < 3 else 1,
        1: f-1 if f > 1 else 3,
    }.get(g, f)

for Fn in (Silver, Gold):
    print(f"{Fn.__name__}:", sum(Fn(*p) for p in Lines))