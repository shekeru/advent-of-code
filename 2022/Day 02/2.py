Lines = [[{k: v % 3 for v, k in enumerate("ABCXYZ")}[x] for 
    x in ln.split()] for ln in open('2022/Day 02/input.txt')]

def Silver(f, g):
    return 1 + (f - g + 1) % 3 * 3 + g

def Gold(f, g):
    return 1 + (g + f - 1) % 3 + 3 * g
    
for Fn in (Silver, Gold):
    print(f"{Fn.__name__}:", sum(Fn(*p) for p in Lines))
