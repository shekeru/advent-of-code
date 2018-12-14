u, v, xs, code = 0, 1, [3,7], "030121"
fmt = lambda x: "".join(map(str,x))
while(code not in fmt(xs[-7:])):
    xs += [*map(int, f"{xs[u] + xs[v]}")]
    u,v = (u+xs[u]+1)%len(xs), (v+xs[v]+1)%len(xs)
offset = 6 if int(code[-1]) == xs[-1] else 7
print('Silver:', fmt(xs[int(code):][:10]))
print('Gold:', len(xs) - offset)
