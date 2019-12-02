def eval(xs, n = 12, v = 2)
  j, xs = -4, xs.clone
  xs[1], xs[2] = n, v
  while xs[j += 4] != 99
    op, a, b, c = xs[j, 4]
    ll = [a, b].map(&->(i: Int32) {xs[i]})
    xs[c] = op.odd? ? ll.sum : ll.product
  end; xs.first
end

def solve(xs, t = 19690720)
  b = eval(xs, 0, 0)
  mj = eval(xs, 1, 0) - b
  v = (t -= b) % (n = t / mj)
  [100 * n, v].sum
end

xs = File.read("input.txt").split(",").map(&.to_i)
puts "Silver: #{eval(xs)}", "Gold: #{solve(xs)}"
