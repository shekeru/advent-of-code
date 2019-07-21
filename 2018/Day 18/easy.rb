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
      [*(-1..1)].product([*(-1..1)]).reduce(0) do |s, (y, x)|
        s + if world[@y+y, @x+x]&.state == type and \
    [y, x] != [0, 0] then 1 else 0 end end end
    # Update Cell State
    puts "X: #{@x}, Y: #{@y}, State: #{@state}, #{[check.call(:trees), check.call(:lumber)]}"
    @state = case @state
      when :lumber
        unless check.call(:lumber).zero? or
            check.call(:trees).zero? then
          :lumber else :open end
      when :trees
        if check.call(:lumber) >= 3 then
          :lumber else :trees end
      when :open
        if check.call(:trees) >= 3 then
          :trees else :open end
    end; self
  end
  # Select Color
  def color
    Color.coerce case @state
      when :lumber; "#FF4136"
      when :trees; "#0074D9"
      when :open; "#111111"
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
    @y, @x = 1, 0
    File.open(fname) do |file|
      file.read.chop.each_char do |chr|
        if chr == "\n" then [@y += 1, @x = 0] else
          self[@y, @x+=1] = Tile.new(@y, @x, chr)
        end
      end
    end
  end
  # Step Forwards
  def step(n = 10)
    @image = Image.new(@x, (n+1) * (@y + 1))
    render; n.times do |i| merge Hash[self.map\
      {|k, value| [k, value.update(self)]}]
    render(i+1) end
    @image.save("debug.bmp", :bmp)
    return self
  end
  # Count & Multiply
  def resolve
    select{|_, t| t.state == :lumber}.count \
    * select{|_, t| t.state == :trees}.count
  end
  # Display Map
  def render(z = 0)
    @y.times do |y| @x.times do |x|
      @image[x, z + (z * @y) + y] = self[y+1, x+1].color
    end end; @image[0..@x-1, z + (z + 1) * @y] \
      = Image.new @x, 1, (Color.coerce "#01FF70")
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
example.step 2
puts example.resolve
