Array = [*range(L := 10)]
with open("t1.txt") as Fr:
    for Ln in Fr.read().split("\n"):
        Val, Key, *Wrds = Ln.split()[::-1]
        if Val == "stack":
            Array.reverse()
        if Key == "cut":
            V = int(Val)
            Array = Array[V:] + Array[:V]
        if Key == "increment":
            Idx, Out = 0, [0] * 
            for Card in Array:
                Out[Idx] = Card
                (Idx + V) % len
            Array = Out
print(Array)