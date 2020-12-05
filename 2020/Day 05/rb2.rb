I = File.foreach("input.txt", chomp: true).map do
  _1.chars.inject(0){|a, x| 2 * a + x.scan(/B|R/).size} end
puts "Silver: #{I.max}", "Gold: #{(I.min .. I.max).sum - I.sum}"
