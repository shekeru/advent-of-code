from copy import deepcopy
State, Seen = [[int(x == '#') for x in y] for y in '''
    .##..
    ##.#.
    ##.##
    .#..#
    #.###
'''.split()], set()
def Nearby(x, y):
    for j in (1, -1):
        yield x + j, y
        yield x, y + j
def Step():
    Temp = deepcopy(State)
    for Y, Ln in enumerate(Temp):
        for X, Ch in enumerate(Ln):
            Count = 0
            for A, B in Nearby(X, Y):
                try:
                    if A >= 0 and B >= 0:
                        Count += Temp[B][A]                        
                except:
                    pass
            if Ch and Count != 1:
                State[Y][X] = 0
            if not Ch and Count in (1, 2):
                State[Y][X] = 1
def Hash():
    return int("".join(("".join(map(str, Ln)) for Ln in State))[::-1], 2)
while (h := Hash()) not in Seen:
    Seen.add(h); Step()
print('Silver:', h)
