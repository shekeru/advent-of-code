with open('input.txt', 'r') as f:
    xs = [*map(int, f.read().split())]
def mk_tree(childs, metas, *xs):
    xs, ts = mk_node(childs, xs, [])
    node = (ts, xs[:metas])
    return (xs[metas:], node)
def mk_node(childs, xs, ts):
    for _ in range(childs):
        xs, node = mk_tree(*xs)
        ts.append(node)
    return (xs, ts)
tree = mk_tree(*xs)[1]
def silver(childs, metas):
    return sum(metas) + sum(silver(*ch)
        for ch in childs)
def gold(childs, metas):
    return sum(metas) if not childs else sum(
        gold(*childs[v-1]) for v in metas if v <= len(childs))
print("Silver:", silver(*tree))
print("Gold:", gold(*tree))
