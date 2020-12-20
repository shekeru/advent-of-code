import itertools, collections, math, queue, re
Basic, Side = lambda X: [X, flipX(X), flipY(X), rotateL(X), rotateR(X),
    rotateL(rotateL(X)), rotateL(flipX(X)), rotateL(flipY(X))
], lambda V, X: [L[X] for L in V]; Monster = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
] # Functions
rotateR = lambda V: [*zip(*V[::-1])]
rotateL = lambda V: [*zip(*V)][::-1]
flipX = lambda V: [L[::-1] for L in V]
flipY = lambda V: V[::-1]
# Import Data
Tile = {int(Hd.split()[1][:-1]): Basic([*map(tuple, Ln)]) for (Hd, *Ln) in
    (x.strip().split('\n') for x in open('Day 20/input.txt').read().split('\n\n'))}
BorderRemove = lambda V: [x[1:-1] for x in V[1:-1]]
Images, Bounds = [], int(math.sqrt(len(Tile)))
# Functions for Graph
def CheckConnect(A, B):
    if A[-1] == B[0]:
        return 0, -1
    if A[0] == B[-1]:
        return 0, 1
    if Side(A, -1) == Side(B, 0):
        return -1, 0
    if Side(A, 0) == Side(B, -1):
        return 1, 0
def GetDelta(A, B):
    if (T := CheckConnect(A, B)):
        def Modify(X, Y):
            X, Y = X + X0, Y + Y0
            if 0 <= X < Bounds and 0 <= Y < Bounds:
                return X, Y
        X0, Y0 = T
        return Modify
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
                    V = (Rt + 1, Pt_, Ki_2)
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
                for Ix, Ln in enumerate(BorderRemove(Tile[ID][Spin])):
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
    Aids = sum(L.count("#") for L in Data)
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
    return (Aids - Total * 15) if Total else 0
# Just Kill Me
print("Silver:", math.prod({K for K, I in Corners}))
print("Gold:", sum(SearchLoop(X) for X in Images))
