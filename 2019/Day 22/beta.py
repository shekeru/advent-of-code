I, L = 2019, 10007
# The Fuck is this Shit
for Ln in open("input.txt"):
    Val, Key, *Wrds = Ln.split()[::-1]
    if Val == "stack":
        I = -(I + 1) % L
    else:
        V = int(Val)
    if Key == "increment":
        I = (I * V) % L
    elif Key == "cut":
        I = (I - V) % L
print("Silver:", I)