# Function
class Array
    def is_valid
        a, b, c = self
        b + c > a &&
        a + c > b &&
        b + a > c
    end
end
# Filter Out Numbers
lines = File.read_lines("input.txt")
xss = lines.map(&.split(" ") \
    .reject("").map(&.to_i))
# Prepare Answers
part1 = xss.select(&.is_valid) 
part2 = xss.transpose.reduce{|ys, x| ys.concat(x)
    }.each_slice(3).select(&.is_valid)
# Display Answers
puts "Silver: #{part1.size}"
puts "Gold: #{part2.size}"
