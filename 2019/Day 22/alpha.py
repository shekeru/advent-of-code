def Execute(name, Copy = ()):
    Array = [*range(L := len(Copy) or 10007)]
    with open(f"{name}.txt") as Fr:
        for Ln in Fr.read().split("\n"):
            Val, Key, *Wrds = Ln.split()[::-1]
            if Val == "stack":
                Array.reverse()
                continue
            V = int(Val)
            if Key == "cut":
                Array = Array[V:] + Array[:V]
            elif Key == "increment":
                Idx, Out = 0, [0] * L
                for Card in Array:
                    Out[Idx % L] = Card
                    Idx += V
                Array = Out
    if Array == Copy:
        print(name, "OK!") 
    return Array
# Test Cases
Execute("t1", [0, 3, 6, 9, 2, 5, 8, 1, 4, 7])
Execute("t2", [3, 0, 7, 4, 1, 8, 5, 2, 9, 6])
Execute("t3", [6, 3, 0, 7, 4, 1, 8, 5, 2, 9])
Execute("t4", [9, 2, 5, 8, 1, 4, 7, 0, 3, 6])
# Silver
Array = Execute("input")
print("Silver:", Array.index(2019))