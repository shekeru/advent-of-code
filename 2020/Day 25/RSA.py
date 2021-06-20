import math
# Constants
Base, Modulo = 7, 20201227
Card, Door = 6552760, 13233401
# Naive Brute Force Approach
def BruteForce(Keys, A = 1, Loop = 0):
    while Loop := Loop + 1:
        if (A := (A * Base) % Modulo) in Keys:
            Keys.remove(A); return Keys[0], Loop
print("BruteForce:", pow(*BruteForce([13233401, 6552760]), Modulo))
# Discrete Logarithm Solution
Alt, Table = pow(Base, (Modulo - 2) * (Upper := math.ceil(math.sqrt(Modulo - 1))),
    Modulo), {pow(Base, Loop, Modulo): Loop for Loop in range(1, Upper)}
for Exponent in range(1, Upper):
    if (Y := Card * pow(Alt, Exponent, Modulo) % Modulo) in Table:
        print("Fermat's:", pow(Door, Exponent * Upper + Table[Y], Modulo)); break
