from itertools import accumulate, product
pr = {'R': complex(1), 'L': complex(-1), 'U': 1j, 'D': -1j}
with open("2019/Day 03/input.txt") as f:
    fn = lambda x: pr[x[0]] * int(x[1:])
    xss = [(*map(fn, xs.split(',')),)
        for xs in f.readlines()]

def abg(PTS):
    dtr = lambda a,b: (a[0] * b[1]) - (a[1] * b[0])
    xdf = lambda v: abs(v[1].real - v[0].real)
    ydf = lambda v: abs(v[1].imag - v[0].imag)
    xds, yds = [*map(xdf, PTS)], [*map(ydf, PTS)]
    if dtr(xds, yds):
        xi, yi = xds.index(max(xds)), yds.index(max(yds))
        X0, X1, Y0, Y1 = PTS[xi] + PTS[yi]
        if ((X0.real <= Y0.real <= X1.real or X0.real >= Y0.real >= X1.real)
    and (Y0.imag <= X1.imag <= Y1.imag or Y0.imag >= X1.imag >= Y1.imag)):
            crn = [yss[ll][pts[ll].index(pp) - 1] for ll, pp in enumerate(PTS)]
            offset = abs(Y0.real - X0.real) + abs(X1.imag - Y0.imag)
            return mdt(complex(Y0.real, X1.imag)), sum(crn) + offset

acc = lambda xs: [*accumulate(xs)]
mdt = lambda x: abs(x.real) + abs(x.imag)
yss = [acc(map(mdt, xs)) for xs in xss]
pts = [[*zip([0, *rgs], rgs)] for rgs in map(acc, xss)]
p1, p2 = map(min, zip(*filter(None, map(abg, [*product(*pts)]))))

print("Silver: %d" % p1)
print("Gold: %d" % p2)
