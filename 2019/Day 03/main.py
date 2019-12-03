with open("2019/Day 03/input.txt") as f:
    fn = lambda x: (x[0], int(x[1:]))
    xs = [fn(x) for x in f.read().split(',')]
