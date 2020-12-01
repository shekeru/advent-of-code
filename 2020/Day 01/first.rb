I = File.readlines('input.txt').map(&:to_i)
def sv(x) I.combination(x).find{2020 == _1.sum}.inject(:*)
  end; puts "Silver: #{sv 2}", "Gold: #{sv 3}"
