$val = {} of (String | Nil) => (Int32)
tree = {} of (String | Nil) => (String | Nil)
# Parse data on Lines
lines = File.read_lines("ins.txt")
  .map(&.scan(/\w+/).map(&.to_a.first))
# Tree Structure
lines.each do |ln|
  $val[ln[0]] = (ln[1] || "0").to_i
  ln[2..-1].each do |ch|
    tree[ch] = ln[0]
end end
# Silver, Find Root
root = tree.first_key
while tree.has_key? root
  root = tree[root] end
# Printing
puts "Silver: #{root}"
