from re import findall
# Structure
class Node:
    Graph = {}
    def __init__(self, N, W, *Ch):
        Node.Graph[N] = self
        self.children = Ch
        self.weight = int(W)
        self.ID = N
    def update_children(self):
        self.children = [*map(Node.Graph
            .get, self.children)]
    def list(self):
        yield self.weight
        for Ch in self.children:
            yield sum(Ch.list())
    def balance(self, delta = 0):
        array = [*self.list()][1:]
        for w in array:
            if array.count(w) == 1:
                dt = ({*array} - {w}).pop() - w
                Ch = self.children[array.index(w)]
                return Ch.balance(dt)
        return self.weight + delta
# Load Input
for ln in open("2017/Day 07/ins.txt"):
    Node(*findall(r'\w+', ln.strip()))
# Add Parents, Update Children
for Pr in Node.Graph.values():
    Pr.update_children()
    for Ch in Pr.children:
        Ch.parent = Pr
# Find Root
while hasattr(Pr, 'parent'):
    Pr = Pr.parent
# Fuck This Shit
print("Silver:", Pr.ID)
print("Gold:", Pr.balance())
