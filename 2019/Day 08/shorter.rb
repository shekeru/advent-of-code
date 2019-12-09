first = (layers = *File.read('ins.txt').strip
  .chars.each_slice(150)).min_by{|x| x.count(?0)}
# Display Everything
puts "Silver: #{first.count(?1) * first.count(?2)}",
  layers.transpose.map{|xs| xs.delete(?2); xs}.map{|x|
    ?1 == x.first ? '■':' '}.each_slice(25).map(&:join)
