class World < Hash
  def initialize(xs)
    @stack = Array.new
    self[0, 0] = [nil, 0]
    xs.strip.chars. \
      each(&method(:eval))
  end
  # Logic
  def eval(dir)
    case dir; when '^'
      @stack.push [0,0]
    when '('
      @stack.push @stack[-1]
    when '|'
      @stack[-1] = @stack[-2]
    when ')'
      @stack.pop
    when '$'
      nil#puts self
    else
      march(dir)
    end
  end
  def march(dir)
    @stack[-1] = [ptr = \
    @stack[-1], case dir
      when 'N'; [+1, 0]
      when 'S'; [-1, 0]
      when 'W'; [0, -1]
      when 'E'; [0, +1]
    end].transpose.map{|x| x.reduce(:+)}
    self[*@stack[-1]] = [ptr, 1 + self[*ptr] \
      .last] unless self[*@stack[-1]]
  end
  # Solutions
  def silver
    values.map(&:last).max
  end
  def gold
    values.map(&:last).select{
      |x| x >= 1000}.count
  end
  # Improve Hash Access
  def []=(y, x, v)
    self.store([y,x], v)
  end
  def [](y, x)
    self.fetch([y,x], nil)
  end
end
# Read File
def multiline(fname)
  File.readlines(fname).map \
    {|regex| World.new(regex)}
end
# Test Cases
raise "error." unless multiline("example.txt") \
  .map(&:silver) == [3, 10, 18, 23, 31]
# Solve Day
world = multiline('input.txt')[0]
puts "Silver: #{world.silver}"
puts "Gold: #{world.gold}"
