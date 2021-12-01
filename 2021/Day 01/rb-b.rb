I = File.readlines("i1.txt").map(&:to_i)

def solve(n)
  I.zip(I.drop n).count{_2.to_i > _1}
end; puts "Silver: #{solve 1}",
  "Gold: #{solve 3}"
