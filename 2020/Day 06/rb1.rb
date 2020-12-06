I = open("input.txt").read.split("\n\n")
puts "Silver: #{I.sum{_1.split.join.chars.uniq.size}}"
puts "Gold: #{I.sum{|x| x.split.map(&:chars).reduce{_1&_2}.size}}"
