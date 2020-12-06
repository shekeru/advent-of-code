print("Silver: %d\nGold: %d\n" %tuple(sum(len(F(*map(set, X.split()))) for X in
    open("input.txt").read().split("\n\n")) for F in (set.union, set.intersection)))
