chars = File.read("input.txt").strip.chars
floors = chars.reduce([0]) do |a, e|
  a.push a[-1] + (e == ')' ? -1:1)
end; puts "Silver #{floors.last}",
  "Gold: #{floors.index(-1)}"
