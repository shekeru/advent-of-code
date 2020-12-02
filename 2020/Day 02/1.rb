I = File.readlines('input.txt').map do
  n, c, p = _1.split; [n.split(?-).map(&:to_i), c[0], p]
end; puts "Silver: #{I.count{|(n, c, p)| p.count(c).between?(*n)}}",
  "Gold: #{I.count{|(n, c, p)| n.map{p[_1 - 1]}.count(c) == 1}}"
