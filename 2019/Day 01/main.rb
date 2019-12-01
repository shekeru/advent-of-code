ys, xs = Array.new, File.
  readlines('input.txt').map(&:to_i)
while xs.any?{|x| x > 0}
  ys << xs.map!{|x| [0,
    x/3 - 2].max}.sum end
puts "Silver: #{ys.first}",
  "Gold: #{ys.sum}"
