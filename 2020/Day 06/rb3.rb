printf "Silver: %d\nGold: %d\n", *[:|, :&].map{|f|
  File.read("input.txt").split("\n\n").map \
{_1.split.map(&:chars)}.sum{_1.reduce(f).size}}
