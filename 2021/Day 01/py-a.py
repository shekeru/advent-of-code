# Hello Again Old Friends
def f(*X):
    return (*map(*X),)
def z(K, N):
    return zip(*(K[J:] for J in range(N)))
def w(I, O):
    return sum(int(B > A) for A, B in z(f(sum, z(I, O)), 2))
# I've had such a strssful year
with open('i1.txt') as X:
    I = f(int, X.read().split())
# this is fun atleast
print("silver:", w(I, 1))
print("gold:", w(I, 3))
