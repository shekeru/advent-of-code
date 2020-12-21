import functools, re
Pr = re.compile("((?: ?\w+)+) \(contains((?: \w+,?)+)")
Ae = [({Y.strip() for Y in Ys.split(',')}, {*Xs.split()}) for
    Xs, Ys in Pr.findall(open("Day 21/input.txt").read())]
Pt, Et = {X: functools.reduce(set.intersection, (Ys for Hd, Ys in Ae if X in Hd))
    for X in {Hx for Hd, _ in Ae for Hx in Hd}}, {}
print("Silver:", len([Bx for _, Bd in Ae for Bx in Bd if
    Bx not in functools.reduce(set.union, Pt.values())]))
while Pt:
    Tx, Ix = next((Tx, Ix) for Tx, Ix in Pt.items() if len(Ix) == 1)
    Pt = {K: V - Ix for K, V in Pt.items() if K != Tx}; Et[Tx] = Ix.pop()
print("Gold:", ",".join(Et[X] for X in sorted(Et)))
