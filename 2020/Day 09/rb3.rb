V = File.read("input.txt").split.map(&:to_i)
X = V[25..].find.with_index{ !V[_2, 25]
  .combination(2).map(&:sum).include? _1}
a, b = 0, 1; while X != k = (s = V[a..b]).sum do
  if k > X then a += 1 else b += 1 end end
puts "Silver: #{X}", "Gold: #{s.minmax.sum}"
