# def Combinations(A, M):
#     if not M:
#         yield []
#         return
#     if not A:
#         return []
#     for L in Combinations(A[1:], M-1):
#         yield A[:1] + L
#     yield from Combinations(A[1:], M)

def Tails(Array):
    for x in range(1, len(Array)):
        yield Array[x:]

def C2(Array, M):
    if not M:
        yield []; return
    for (First, *Others) in Tails(Array):
        for Ys in C2(Others, M - 1):
            yield [First] + Ys

def Product(A, V = 1):
    return Product(A[1:], A[0] * V) if A else V

def Solve(Rn):
    return Product({sum(Y): Y for Y in C2(Xs, Rn)}[2020])

Xs = [int(x) for x in open('input.txt')]
print("Silver:", Solve(2))
print("Gold:", Solve(3))
