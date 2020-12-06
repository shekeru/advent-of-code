I = File.read("input.txt").split("\n\n").map{_1.split.map(&:chars)}
puts "Silver: #{I.sum{_1.reduce(:|).size}}",
  "Gold: #{I.sum{_1.reduce(:&).size}}"
