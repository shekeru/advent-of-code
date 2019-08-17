lines = File.read_lines("input.txt")
# Format Initial Sets
words = lines.map do |ln|
    orig = ln.split " "
    hash = orig.to_set
    [orig, hash]
end
# Part One
valid = words.select do |(o, n)|
    o.size == n.size
end; puts "Silver: #{valid.size}"
# Part Two
safer = valid.select do |(o, n)|
    n.map(&.chars.sort) \
        .to_set.size == o.size
end; puts "Gold: #{safer.size}"
