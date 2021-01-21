A, B = map(lambda x: [*map(int, x.split()[2:])],
    open("2020/Day 22/input.txt").read().split('\n\n'))
# Part 1
def Score(*Decks):
    return sum(F * V for F, V in enumerate(sum(Decks, [])[::-1], 1))
def Turn(X, Y, A, B):
    if X > Y:
        A += [X, Y]
    else:
        B += [Y, X]
    return A, B
def Straight(A, B):
    while A and B:
        X, Y = A.pop(0), B.pop(0)
        Turn(X, Y, A, B)
    return A, B
# Part 2
def Recurse(A, B):
    States = set()
    while A and B:
        T = tuple(A), tuple(B)
        if T in States:
            return [1], []
        States.add(T)
        X, Y = A.pop(0), B.pop(0)
        if len(A) >= X and len(B) >= Y:
            F, G = Recurse(A.copy()[:X], B.copy()[:Y])
            if F:
                A += [X, Y]
            else:
                B += [Y, X]
        else:
            A, B = Turn(X, Y, A, B)
    return A, B
# Results
print("Silver:", Score(*Straight(A.copy(), B.copy())))
print("Gold:", Score(*Recurse(A.copy(), B.copy())))
