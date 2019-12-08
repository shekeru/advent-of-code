layers = File.read('ins.txt').strip
  .chars.each_slice(150).to_a
# Part 1 Min
mins = layers.min_by{|xs|
  xs.count{|x| '0' == x}}
# Part 2 Text
pixels = layers.reverse.transpose.map{
  |xs| xs.inject{|a, e| '2' == e ? a : e}
}.map{|x| '1' == x ? '■':' '}.
  each_slice(25).map(&:join)
# Display Everything
puts "Silver: #{"12".chars.map{|c| mins
  .count{|x| c == x}}.inject(:*)}", pixels
