I = File.readlines("i1.txt").map(&:to_i)

def solve(xs)
  xs.each_cons(2).count{_2 > _1}
end

puts "Silver: #{solve I}",
  "Gold: #{solve I.each_cons(3).map(&:sum)}"
