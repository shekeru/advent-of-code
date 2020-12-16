import re, itertools
File = [re.sub(r"mask = ([01X]+)",
    r'mem.mask = "\1"', Ln) for Ln in
open('Day 14/input.txt')]
# Shared Class
class Shared(dict):
    def __call__(mem):
        for Ln in File: exec(Ln)
        print(mem.__class__.__name__ \
            + ':', sum(mem.values()))
# Part One
class Silver(Shared):
    def __setitem__(mem, k, v):
        A = int(mem.mask.replace('X', '1'), 2)
        B = int(mem.mask.replace('X', '0'), 2)
        super().__setitem__(k, v & A | B)
# Part Two
class Gold(Shared):
    def __setitem__(mem, k, v):
        B = int(mem.mask.replace('X', '0'), 2)
        Ix = [I for I, F in enumerate(mem.mask) if F == 'X']
        Real = ['0' if I in Ix else F for I, F in enumerate \
            (list(bin(k | B)[2:].rjust(36, '0')))]
        for L in range(len(Ix)+1):
            for Bits in itertools.combinations(Ix, L):
                Key = Real.copy()
                for Bit in Bits:
                    Key[Bit] = '1'
                super().__setitem__(int("".join(Key), 2), v)
# Results
Silver()(), Gold()()
