I = [[*map(set, Zn.split())] for Zn in open("input.txt").
    read().split("\n\n")]; print("Silver:",
sum(len(set.union(*Zn)) for Zn in I), "\nGold:",
sum(len(set.intersection(*Zn)) for Zn in I))
