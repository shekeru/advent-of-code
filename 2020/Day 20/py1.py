import itertools, collections, math, queue
Images, Monster, Bounds = [], [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
], int(math.sqrt(len(Tile)))
# Prepare Tile Array
def Translate(X):
    for _ in range(4):
        yield (X := [*zip(*X)])
        yield (X := X[::-1])
Tile = {int(Hd.split()[1][:-1]): [*Translate([*map(tuple, Ln)])] for (Hd, *Ln) in
    (x.strip().split('\n') for x in open('Day 20/input.txt').read().split('\n\n'))}
B_Strip, Fs = lambda V: [x[1:-1] for x in V[1:-1]], lambda V, X: [L[X] for L in V]
# Functions for Graph
def CheckConnect(A, B):
    if A[-1] == B[0]:
        return 0, -1
    if A[0] == B[-1]:
        return 0, 1
    if Fs(A, -1) == Fs(B, 0):
        return -1, 0
    if Fs(A, 0) == Fs(B, -1):
        return 1, 0
def GetDelta(A, B):
    if (T := CheckConnect(A, B)):
        def Modify(X, Y):
            X, Y = X + X0, Y + Y0
            if 0 <= X < Bounds and 0 <= Y < Bounds:
                return X, Y
        X0, Y0 = T; return Modify
# Find Connections
Graph = collections.defaultdict(dict)
for K1, K2 in itertools.permutations(Tile, 2):
    for I, A in enumerate(Tile[K1]):
        for J, B in enumerate(Tile[K2]):
            if (T := GetDelta(B, A)):
                Graph[K1, I][K2, J] = T
# Graph Search
def GenMAP(Initial):
    Seen = {(0, 0): Initial}
    Next = queue.PriorityQueue()
    Next.put((0, (0, 0), Initial))
    while not Next.empty():
        Rt, Pt, Ki_1 = Next.get()
        for Ki_2 in (Fn := Graph[Ki_1]):
            if (Pt_ := Fn[Ki_2](*Pt)):
                if Pt_ not in Seen:
                    V = (1 + Rt, Pt_, Ki_2)
                    Seen[Pt_] = Ki_2
                    Next.put(V)
    return Seen
# WTF AM DO
for Ki in (Corners := {Ki for Ki in sorted(Graph) if len({*Graph[Ki].items()}) == 2}):
    if len(V := GenMAP(Ki)) == Bounds ** 2 and not (Flat_Image := []):
        for Y in range(Bounds):
            Current = [""] * 8
            for X in range(Bounds):
                ID, Spin = V[X, Y]
                for Ix, Ln in enumerate(B_Strip(Tile[ID][Spin])):
                    Current[Ix] += "".join(Ln)
            Flat_Image += Current
        Images.append(Flat_Image)
# Search for Dragons
def SearchHere(Data, MP):
    for Start in range(len(Data) - len(MP)):
        for I, Ch in enumerate(MP):
            if not (" " == Ch or Data[Start+I] == Ch):
                break
        else:
            yield Start
    return []
def SearchLoop(Data, Total = 0):
    Base = sum(L.count("#") for L in Data)
    for L in range(len(Data) - 3):
        Prev = set()
        for I in range(3):
            F = {*SearchHere(Data[L+I], Monster[I])}
            if I == 0 and F:
                Prev |= F
            elif Prev & F:
                Prev &= F
            else:
                break
        else:
            Total += len(Prev)
    return (Base - Total * 15) if Total else 0
# Just Kill Me
print("Silver:", math.prod({K for K, I in Corners}))
print("Gold:", sum(SearchLoop(X) for X in Images))
