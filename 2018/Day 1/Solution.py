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

frequency = 0
with open("input.txt", "r") as fp:
    for line in fp:
        if line[0] == "+":
            frequency += int(line[1:-1])
        else:
            frequency -= int(line[1:-1])
print(f"Final frequency: {frequency}")

frequencies = open("input.txt", "r").read().strip().split("\n")
total_frequency = 0
previous_freqs = {0}
while True:
    for frequency in frequencies:
        if frequency.startswith("+"):
            total_frequency += int(frequency[1:])
        else:
            total_frequency -= int(frequency[1:])
        if total_frequency in previous_freqs:
            print(f"Duplicate frequency: {total_frequency}")
            exit()
        previous_freqs.add(total_frequency)
