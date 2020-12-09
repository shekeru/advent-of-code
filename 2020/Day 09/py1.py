from itertools import combinations
Arr = [*map(int, open('2020/Day 09/input.txt'))]
# Efficientish Search
def Weakness(V):
    for Y in range(2, len(Arr)):
        for A in range(1 + len(Arr) - Y):
            if sum(S := Arr[A:A+Y]) == V:
                return min(S) + max(S)
            elif sum(S) > V:
                break
# Find A Weakness
print("Silver:", V := Arr[next(filter(lambda I: Arr[I]
    not in map(sum, combinations(Arr[I-25:I], 2)),
range(25, len(Arr))))], "\nGold:", Weakness(V))
