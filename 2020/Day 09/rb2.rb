V = File.read("input.txt").split.map(&:to_i)
X = V.drop(25).map.with_index{ _1 unless
  V[_2, 25].combination(2).map(&:sum).include? _1
}.compact.first; def exploit a = 0, b = 1
  while X != k = (s = V[a..b]).sum do
    if k > X then a += 1 else b += 1
end end; s.minmax.sum end; puts \
  "Silver: #{X}", "Gold: #{exploit}"
