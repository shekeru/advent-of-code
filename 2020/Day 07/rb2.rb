Graph, T = File.read("input.txt").split(?\n).map{
  |ln| (_, m), *xs = ln.scan(/(^|\d\s)(\w+\s\w+)/)
[m, xs.map{[_1.to_i, _2]}]}.to_h, "shiny gold"
# Silver Solution
def silver wh
  return T == wh || Graph[wh].any?{silver _1[1]}
end; puts "Silver: #{Graph.count{silver _1[0]} - 1}"
# Gold Solution
def gold wh
  Graph[wh].sum{_1 + gold(_2) * _1}
end; puts "Gold: #{gold T}"
