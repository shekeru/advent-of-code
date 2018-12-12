from collections import defaultdict
init = lambda xvs: defaultdict(lambda: '.', xvs)
with open('input.txt') as f:
    state, _, *trans = f.read().splitlines()
state = init(enumerate(state.split(': ')[-1]))
trans, const = dict(map(lambda x: x.split(' => '), trans)), 50000000000
get_keys, delta = lambda: {k for k,v in state.items() if v == '#'}, 0
for i in range(1, const+1):
    keys = get_keys(); last, low, high = sum(keys), min(keys), max(keys)
    state = init({k: trans.get("".join([state[x] for x in range(k-2, k+3)]),
        state[k]) for k in range(low-2, high+3)})
    if i is 20:
        print('Silver:', sum(get_keys()))
    elif sum(get_keys()) - last != delta:
        delta = sum(get_keys()) - last
    else:
        break
print("Gold:", sum(get_keys())+(const-i)*delta)
