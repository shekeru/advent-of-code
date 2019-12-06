$sys = Hash.new; require 'set'
File.read("input.txt").split.each do
  |ln| pr, ch = ln.split(')')
$sys[ch] = pr end
# Iterate Backwards
def flatten(x)
  Set.new(Enumerator.new do
    |en| while $sys.key? x
      en.yield (x = $sys[x])
  end end)
end
# Such a nice day
puts "Silver: #{$sys.keys.map{|x| flatten(x).size}.sum}",
  "Gold: #{(flatten('SAN') ^ flatten('YOU')).size}"
