Array = [*enumerate([1,2,16,19,18,0], 1)]
# Fucking Hell
def AidsDict(Nth):
    Turn, Spoken = Array[-1]
    Graph = {V: (K, 0) for K, V in Array}
    while Nth > Turn:
        Turn += 1
        Last, Prev = Graph[Spoken]
        Spoken = Last - Prev if Prev else 0
        Keep, _ = Graph.get(Spoken, (0, 0))
        Graph[Spoken] = (Turn, Keep)
    return Spoken
# Results
print("Silver:", AidsDict(2020))
print("Gold:", AidsDict(30000000))
