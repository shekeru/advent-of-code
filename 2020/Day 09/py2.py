from itertools import combinations
Arr = [*map(int, open('2020/Day 09/input.txt'))]
# Efficientish Search
def Weakness(V, A = 0, B = 2):
    while V != (K := sum(S := Arr[A:B])):
        if K > V: A += 1
        else: B += 1
    return min(S) + max(S)
# Find A Weakness
print("Silver:", V := Arr[next(filter(lambda I: Arr[I]
    not in map(sum, combinations(Arr[I-25:I], 2)),
range(25, len(Arr))))], "\nGold:", Weakness(V))
