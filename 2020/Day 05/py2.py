print("Silver:", V := max(F := {int("".join('1' if C in "BR" else '0' for C in
    X.strip()), 2) for X in open("input.txt")}), "\nGold:", max({*range(V)} - F))
