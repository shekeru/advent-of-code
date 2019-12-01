with open("2019/Day 01/input.txt") as f:
    xs = [int(x) for x in f.readlines()]
# Evaluate
values = list()
fuel = lambda x: max(0, x//3 - 2)
while any(xs):
    xs = [*map(fuel, xs)]
    values.append(sum(xs))
# Display
print("Silver:", values[0])
print("Gold:", sum(values))
