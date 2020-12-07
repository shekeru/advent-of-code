Graph = File.read("input.txt").split(?\n).map{|ln|
  (_, m), *xs = ln.scan(/(^|\d\s)(\w+\s\w+)/)
[m, xs.map{[_1.to_i, _2]}]}.to_h
# Silver Solution
def silver wh
  Graph.map{|k, v| [k, *silver(k)] if
    v.map{_2}.include? wh}.compact.flatten
end; puts "Silver: #{silver("shiny gold").uniq.size}"
# Gold Solution
def gold wh
  Graph[wh].sum{_1 + gold(_2) * _1}
end; puts "Gold: #{gold("shiny gold")}"
