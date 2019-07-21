inputs = File.readlines('input.txt').map do
  |ln| ln.strip.split("x").map(&:to_i) end
lengths = inputs.map do |ln| sides = ln\
  .combination(2).map{|x| x.inject(:*)}
    sides.min + sides.sum * 2
end; puts "Silver: #{lengths.sum}"
ribbons = inputs.map do |ln| 2 \
  * ln.min(2).sum + ln.inject(:*)
end; puts "Gold: #{ribbons.sum}"
