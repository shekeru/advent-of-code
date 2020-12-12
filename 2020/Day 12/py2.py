M_Dist = lambda: int(abs(Ship.real) + abs(Ship.imag))
# Globals
P, D, R = [(LN[0], int(LN[1:])) for
    LN in open('Day 12/input.txt')], {
'N': 1j, 'E': 1, 'S': -1j, 'W': -1
    }, {'L': 1j, 'R': -1j}
# Part 1
Ship, Head = 0, 1
for O, V in P:
    Ship += D.get(O, 0) * V
    Head *= R.get(O, 1) ** (V/90)
    if O == "F":
        Ship += V * Head
print("Silver:", M_Dist())
# Part 2
Ship, Way = 0, 10+1j
for O, V in P:
    Way += D.get(O, 0) * V
    Way *= R.get(O, 1) ** (V/90)
    if O == "F":
        Ship += V * Way
print("Gold:", M_Dist())
