require 'imageruby'
include ImageRuby
$VERBOSE = nil
class Tile
  attr_accessor :state
  def initialize(y, x, char)
    @state = case char
      when '#'; :lumber
      when '|'; :trees
      when '.'; :open
    end; @y, @x = y, x
  end
  # Transformations
  def update(world)
    # Search Moore neighboorhood
    check = ->(type) do
      [*(-1..1)].product([*(-1..1)]).select{|xs|
        xs.sum}.reduce(0) do |s, (y, x)|
          s + if world[@y+y, @x+x]&.state == type
    then 1 else 0 end end end
    # Update State
    @state = case @state
      when :lumber
        if check.call(:lumber) && check.call(:trees) \
          then :lumber else :open end
      when :trees
        if check.call(:lumber) >= 3 then
          :lumber else :trees end
      when :open
        if check.call(:trees) >= 3 then
          :trees else :open end
    end; self
  end
  # Prettier Print
  def inspect
    @state
  end
end
class World < Hash
  # Parse File into World
  def initialize(fname)
    y, x = 1, 0
    File.open(fname) do |file|
      file.each_char do |chr|
        if chr == "\n" then [y += 1, x = 0] else
          self[y, x+=1] = Tile.new(y, x, chr)
        end
      end
    end
  end
  # Step Forwards
  def step
    merge Hash[map {|k, value|
      [k, value.update(self)]}]
  end
  # Fuck Nested Arrays
  def []=(y, x, v)
    self.store([y,x], v)
  end
  def [](y, x)
    self.fetch([y,x], nil)
  end
end
# Run Example
example = World.new('test.txt')
puts example
puts example.step
