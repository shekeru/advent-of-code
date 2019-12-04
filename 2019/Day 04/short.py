from itertools import groupby

freqs = [{len([*g]) for _, g in groupby(xvs)}
    for xvs in map(lambda x:
        [*str(x)], range(136760, 595730))
    if xvs == sorted(xvs)]

fn = lambda xs: len([*filter(None, xs)])
p1, p2 = [*map(fn, zip(*map(lambda xs:
    (max(xs) >= 2, 2 in xs), freqs)))]

print(f"Silver: {p1}",
    f"Gold: {p2}",
sep = "\n")
