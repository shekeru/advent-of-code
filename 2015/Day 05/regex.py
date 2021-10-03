import re

Checks, Sums = [
    [r"(.*[aeiou]){3}", r".*(.)\1", r".*(ab|cd|pq|xy)"],
    [r".*(..).*\1", r".*(.).\1"],
], [0, 0]

with open('2015/Day 05/input.txt') as F:
    Input = F.read().split()

for Pwd in Input:
    for I, Level in enumerate(Checks):
        Matches = [re.match(Regex, Pwd) for Regex in Level]
        Sums[I] += all(Matches[:2]) and not any(Matches[2:])

print("Solutions:", *Sums)
