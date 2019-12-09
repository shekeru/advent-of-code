part1, part2, stack = 0, 0, 0
# Filter Garbage String
File.read('ins.txt').chomp.gsub(/!./, '')
  .gsub(/<.*?>/){|y| part2 += y.size - 2}
  .each_char do |x| case x
when ?{
  stack += 1
when ?}
  part1 += stack
  stack -= 1
end end
# Display Parts
puts "Silver: #{part1}"
puts "Gold: #{part2}"
