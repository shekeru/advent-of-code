Xa, Yb, Idx = 1, 0, 2020
Iters = 101741582076661
Size = 119315717514047
# Read Instructions
for Ln in open("input.txt"):
    Val, Key, *Wrds = Ln.split()[::-1]
    if Val == "stack":
        a, b = -1, -1
    elif Key == "increment":
        a, b = int(Val), 0
    elif Key == "cut":
        a, b = 1, -int(Val)
    Xa, Yb = a* Xa %Size, \
        (a* Yb +b) %Size
fmt = lambda Val: \
    pow(Val, Size - 2, Size)
# Help, I don't understand this
Mx = pow(Xa, Iters, Size)
Mb = fmt(Xa -1) *(Mx -1) *Yb %Size
# Something, Inverse?
print("Gold:", (Idx -Mb) \
    * fmt(Mx) % Size)