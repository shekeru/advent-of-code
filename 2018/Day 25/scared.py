import re, os
def list_cases(where = '2018/Day 25/'):
    inputs = {}
    for ref in os.listdir(where):
        location = os.path.join(where, ref)
        if '.txt' in location:
            with open(location) as f:
                parse = lambda x: [*map(int, re.findall(r'-?\d+', x))]
                inputs[ref.split('.txt')[0]] = [*map(parse, f.read().splitlines())]
    return inputs
def m_dist(xs, ys):
    solve = lambda x, y: abs(y - x)
    return sum(solve(*pts) for pts in zip(xs, ys))
# Part 1
def group(star, cluster):
    for existing in cluster:
        if m_dist(existing, star) <= 3:
            cluster.append(star)
            return True
def insert(stars):
    consts = list()
    for star in stars:
        appended = [group(star, cluster) for cluster in consts]
        if not [*filter(None, appended)]:
            consts.append([star])
    return consts
# Printing
inputs, correct = list_cases(), [2, 4, 3, 8]
for ref in inputs:
    if 'input' != ref:
        result = insert(inputs[ref])
        nth = int(ref.split('-')[-1])
        print(ref + ',', 'should be',
            correct[nth], 'is', len(result))
#print("Silver:", )
