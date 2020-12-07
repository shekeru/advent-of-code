File.read("input.txt").split("\n\n").then do |x|
  printf "Silver: %d\nGold: %d\n", *[:|, :&].map{|f|
    x.sum{_1.split.map(&:chars).inject(f).size}
}; end
