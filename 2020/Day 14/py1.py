import re; File = [re.sub(r"mask = ([01X]+)",
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
        Ix = [I for I, F in enumerate(mem.mask) if F == 'X']
        Base = mem.mask.replace('X', '0')
        pass
# Results
Silver()(), Gold()()
