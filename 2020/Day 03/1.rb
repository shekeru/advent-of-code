I, V = File.readlines('input.txt'),
  [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

def j(a, b)
  (0..I.count-1).step(b).map{|y|
    I[y][a * y/b % 31]}.count(?#)
end

puts "Silver: #{j(*V[1])}",
  "Gold: #{V.inject(1){j(*_2)*_1}}"
