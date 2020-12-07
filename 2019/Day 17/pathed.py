import re
# Read Map
Path = {}
with open("2019/Day 17/path.txt") as F:
    for Y, Ln in enumerate(F, 1):
        for X, Ch in enumerate(Ln, 1):
            if Ch == "#":
                Path[X, Y] = 1
            if Ch == "^":
                You = X, Y
Face, Past = 0, [You]
# Relative Positions
def Nearby(x, y):
    for j in (1, -1):
        if not Face % 2:
            yield x + j, y
        else:
            yield x, y + j
def AdjustFace(dX, dY):
    global Face
    if Face < 2:
        if dX + dY > 0:
            Face += 1
            S = "R"
        else:
            Face -= 1
            S = "L"
    else:
        if dX+dY > 0:
            Face -= 1
            S = "L"
        else:
            Face += 1
            S = "R"
    Face %= 4
    return S
def Valid(x, y):
    global You
    X, Y = [pr for pr in Nearby(x, y) if
        pr in Path and pr not in Past][0]
    F, dX, dY = 1, X - x, Y - y
    while True:
        End = (x + dX * F, y + dY * F)
        if End in Path:
            F += 1
            Past.append(End)
        else:
            F -= 1
            Past.pop()
            break
    You = (x + dX * F, y + dY * F)
    S = AdjustFace(dX, dY)
    return S+",%s," %F
Turns = ""
while You != (11, 55):
    Turns += Valid(*You)
Sephi = re.compile(r'^(.{1,21})\1*(.{1,21})(?:\1|\2)*(.{1,21})(?:\1|\2|\3)*$')
for G in Sephi.match(Turns).groups():
    print(G)
