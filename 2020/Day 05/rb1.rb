I = File.foreach("input.txt", chomp: true).map {
  _1.chars.inject(0){|a, x| 2 * a + x.scan(/B|R/).size}
}; puts "Silver: #{I.max}",
  "Gold: #{(I.min .. I.max).find{!I.include? _1}}"
