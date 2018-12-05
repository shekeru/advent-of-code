import string, re
with open('input.txt') as f:
    series = f.read().strip()
def linear_react(series, char = ''):
    i, series = 0, [*re.sub(char, '', series, flags = re.I)]
    while i+1 < len(series):
        if series[i].swapcase() == series[i+1]:
            del series[i:i+2]
            i = max(0, i-1)
        else:
            i += 1
    return len(series)
print('part 1:', linear_react(series))
print('part 2:', min(linear_react(series, c)
    for c in string.ascii_uppercase))
