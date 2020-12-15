N, Xs = open('Day 13/input.txt').read().split()
N, Xs = int(N), [int(x) if x != 'x' else 0 for x in Xs.split(',')]
# Part 1
def Silver():
    Ys = sorted(filter(None, Xs), key = lambda x:
        x - N % x); return Ys[0] * (Ys[0] - N % Ys[0])
# Part 2
def Gold(Target = 0, Factor = 1):
    for I, X in filter(lambda x: x[1], enumerate(Xs)):
        while (I + Target) % X:
            Target += Factor
        Factor *= X
    return Target
# Results
print("Silver:", Silver())
print("Gold:", Gold())
