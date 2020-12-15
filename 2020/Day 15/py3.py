Graph = [0] * 30000000
for Turn, Card in enumerate([1,2,16,19,18,0], 1):
    Graph[Card] = Turn
# Fucking Hell
def TurnCards(Nth):
    global Turn, Card
    while Nth > Turn:
        Graph[Card], Card = Turn, Turn - \
            (Graph[Card] or Turn); Turn += 1
    return Card
# Results
print("Silver:", TurnCards(2020))
print("Gold:", TurnCards(30000000))
