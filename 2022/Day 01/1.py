Totals = [0] 

for ln in open('input.txt'):
    if (Str := ln.strip()):
        Totals[-1] += int(Str)
    else:
        Totals.append(0)

Totals = sorted(Totals)
print('silver:', Totals[-1])
print('gold:', sum(Totals[-3:]))
