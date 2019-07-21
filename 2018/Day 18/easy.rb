Lumber = '#'; Trees = '|'; Open = '.'
require 'imageruby'
include ImageRuby
$VERBOSE = nil
class Tile
  attr_accessor :state
  def initialize(y, x, char)
    @state, @y, @x = char, y, x
  end
  # Transformations
  def update(world)
    # Search Moore neighboorhood
    check = ->(type) do
      [*(-1..1)].product([*(-1..1)]).reduce(0) do |s, (y, x)|
        s + if world[@y+y, @x+x]&.state == type and \
    [y, x] != [0, 0] then 1 else 0 end end end
    # Return New Cell State
    Tile.new @y, @x, case @state
      when Lumber
        unless check.call(Lumber).zero? or
            check.call(Trees).zero? then
          Lumber else Open end
      when Trees
        if check.call(Lumber) >= 3 then
          Lumber else Trees end
      when Open
        if check.call(Trees) >= 3 then
          Trees else Open end
    end
  end
  # Select Color
  def color
    Color.coerce case @state
      when Lumber; "#FF4136"
      when Trees; "#0074D9"
      when Open; "#111111"
    end
  end
  # Prettier Print
  def inspect
    @state
  end
end
class World < Hash
  # Parse File into World
  def initialize(fname)
    @nkt, @y, @x = [], 1, 0
    File.open(fname) do |file|
      file.read.chop.each_char do |chr|
        if chr == "\n" then [@y += 1, @x = 0] else
          self[@y, @x+=1] = Tile.new(@y, @x, chr)
    end end end
  end
  # Step Forwards
  def step(limit = 10)
    period = 0; limit.times do |i|
      @nkt.push(resolve); merge!(Hash[map {|k, value| [k, value.update(self)]}])
      if start = @nkt.rindex(resolve) then
        if @nkt.length - start == period then
          return @nkt[-period] if 0 == (limit - @nkt.length) % period
        else period = @nkt.length - start end
    end end; return resolve
  end
  # Count & Multiply
  def resolve
    select{|_, t| t.state == Lumber}.count \
    * select{|_, t| t.state == Trees}.count
  end
  # Display Map
  def render
    @image = Image.new(@x, @y)
    @y.times do |y| @x.times do |x|
      @image[x, y] = self[y+1, x+1].color
    end end; @image.save("debug.bmp", :bmp)
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
testCase = World.new('test.txt')
raise "failed." unless
  testCase.step == 1147
# Solve
world = World.new("input.txt")
puts "Silver: #{world.step}"
puts "Gold: #{world.step(1000000000)}"
