Array = [*enumerate([1,2,16,19,18,0], 1)]
Graph = {V: K for K, V in Array}
Turn, Card = Array[-1]
# Fucking Hell
def TurnCards(Nth):
    global Turn, Card
    while Nth > Turn:
        Graph[Card], Card = Turn, Turn - \
            Graph.get(Card, Turn); Turn += 1
    return Card
# Results
print("Silver:", TurnCards(2020))
print("Gold:", TurnCards(30000000))
