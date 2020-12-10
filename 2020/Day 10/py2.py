from functools import cache, reduce
# UwU, What's this?
def Silver(A, K):
    return (K, *(A[o] + int(o == K-A[0]) for o in [1,2,3]))
At = [*sorted(map(int, open('Day 10/input.txt')))]
Ret = [*reduce(Silver, At, [0, 0, 0, 1])]
# Suck It Incels
@cache
def Gold(V):
    if V not in At or V <= 0:
        return int(not V)
    return sum(Gold(V-o) for o in range(1, 4))
# Trans Rights are Based
print("Silver:", Ret[3] * Ret[1])
print("Gold:", Gold(At[-1]))
