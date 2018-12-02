with open('input.txt') as f:
    xs = [*map(int, f.read().splitlines())]
def cycle(xs):
    seen, current = {0}, 0
    while True:
        for x in [*xs]:
            current += x
            if current in seen:
                return current
            else:
                seen.add(current)
print('part 1:', sum(xs))
print('part 2:', cycle(xs))
input()
