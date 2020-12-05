print("Silver:", V := max(F := {int(X[:-1].translate(str.maketrans('BFRL', '1010')), 2)
    for X in open("input.txt")}), "\nGold:", sum(range(min(F), max(F)+1)) - sum(F))
