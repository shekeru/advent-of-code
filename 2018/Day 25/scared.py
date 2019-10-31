import re, os
def list_cases(where = '2018/Day 25/'):
    inputs = {}
    for ref in os.listdir(where):
        location = os.path.join(where, ref)
        if '.txt' in location:
            with open(location) as f:
                parse = lambda x: (*map(int, re.findall(r'-?\d+', x)),)
                inputs[ref.split('.txt')[0]] = [*map(parse, f.read().splitlines())]
    return inputs
def m_dist(xs, ys):
    solve = lambda x, y: abs(y - x)
    return sum(solve(*pts) for pts in zip(xs, ys))
# Part 1
def mk_clusters(stars):
    inserted, length = set(), len(stars)
    for i in range(length):
        nth, stars[i] = 0, [stars[i]]
        if i in inserted:
            stars[i] = None
            continue
        while nth < len(stars[i]):
            for j in range(i + 1, length):
                if m_dist(stars[i][nth], stars[j]) \
                <= 3 and stars[j] not in stars[i]:
                    stars[i].append(stars[j])
                    inserted.add(j)
            nth += 1
    return [*filter(None, stars)]
# Printing
inputs, correct = list_cases(), [2, 4, 3, 8]
for ref in inputs:
    if 'input' != ref:
        result = mk_clusters(inputs[ref])
        nth = int(ref.split('-')[-1])
        print(ref + ',', 'should be',
            correct[nth], 'is', len(result))
print("Silver:", len(mk_clusters(
    inputs['input'])))
