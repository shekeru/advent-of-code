layers = *File.read('ins.txt').strip.chars.each_slice(150)
first = layers.min_by{|xs| xs.count(?0)}
pixels = layers.reverse.transpose.map{
  |xs| xs.inject{|a, e| '2' == e ? a : e}
}.map{|x| '1' == x ? '■':' '}.each_slice(25).map(&:join)
# Display Everything
puts "Silver: #{first.count(?1) * first.count(?2)}", pixels
