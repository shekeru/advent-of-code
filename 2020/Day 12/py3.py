ShA, ShB, Head, Way = 0, 0, 1, 10+1j
M_Dist = lambda Sh: int(abs(Sh.real) + abs(Sh.imag))
D, R = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}, {'L': 1j, 'R': -1j}
# I love sucking Eric's throbbing, intcode, cock
for O, V in [(L[0], int(L[1:])) for L in open('2020/Day 12/input.txt')]:
    Way *= R.get(O, 1) ** (V/90); Head *= R.get(O, 1) ** (V/90)
    Way += D.get(O, 0) * V; ShA += D.get(O, 0) * V
    if O == "F":
        ShB += V * Way; ShA += V * Head
# Results
print("Silver:", M_Dist(ShA))
print("Gold:", M_Dist(ShB))
