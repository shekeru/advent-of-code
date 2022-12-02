sums = sorted(map(
    lambda xs: sum(map(int, xs.split())),
    open('input.txt').read().split('\n\n')))

print('silver:', sums[-1])
print('gold:', sum(sums[-3:]))
