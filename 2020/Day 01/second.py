def Combinations(A, M):
    if not M:
        yield []
        return
    if not A:
        return []
    for L in Combinations(A[1:], M-1):
        yield A[:1] + L
    yield from Combinations(A[1:], M)

def Product(A, V = 1):
    return Product(A[1:], A[0] * V) if A else V

def Solve(Rn):
    return Product({sum(Y): Y for Y in Combinations(Xs, Rn)}[2020])

Xs = [int(x) for x in open('input.txt')]
print("Silver:", Solve(2))
print("Gold:", Solve(3))
