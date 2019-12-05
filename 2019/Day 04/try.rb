part1 = (136760..595730)
  .map(&:to_s).map(&:chars)
  .select{|xs| xs.sort == xs}
  .map{|xs| xs.slice_when{
    |a, b| a != b}.map(&:size)
  }.reject{|xs| xs.max < 2}

part2 = part1.filter{|xs|
  xs.include? 2}

puts "Silver: #{part1.size}",
  "Gold: #{part2.size}"
