def valid(n):
    v, s = False, str(n)
    for i in range(len(s) - 1):
        v |= s[i] == s[i+1]
        if s[i] > s[i+1]:
             return
    return v

def recheck(n):
    s = str(n)
    for x in {*s}:
        if str(x)*2 in s \
    and str(x)*3 not in s:
            return True

p1 = [*filter(valid,
    range(136760, 595730))]
p2 = [*filter(recheck, p1)]

print("Silver:", len(p1))
print("Gold:", len(p2))
