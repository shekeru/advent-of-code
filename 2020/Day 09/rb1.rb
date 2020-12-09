V = File.read("input.txt").split.map(&:to_i)
X = V.drop(25).map.with_index{ _1 unless
  V[_2, 25].combination(2).map(&:sum).include? _1
}.compact.first; def exploit
  (2..).each do |y| (0..V.size - y).each do |x|
      k = V[x, y]; return k.minmax.sum if
        X == s = k.sum; break if s > X
end; end; end; puts "Silver: #{X}",
  "Gold: #{exploit}"
