require 'imageruby'
include ImageRuby
$VERBOSE = nil
# Helper Class
class Tile
  attr_accessor :type, :y, :x
  def initialize(sys, y, x, t = nil)
    @type, sys[y, x] = t, self
    @sys, @y, @x, = sys, y, x
  end
  # Flow water sideways
  def spill
    #puts "Expanding: #{@y}, #{@x}"
    tiles = [*self.expand([], -1).reverse,
      *self.expand([], 1).drop(1)]
    # Settle water, if bounded
    if tiles.values_at(0, -1).all?(&:solid?) then
      tiles[1..-2].each &->(tile) {
        tile.type = :stable
      }; head = tiles.find \
      {|t| @sys[t.y - 1, t.x]&.water?}
      return @sys[head.y - 1, head.x]
    end; @sys.stack.push \
      *tiles.values_at(0, -1)
    return nil
  end
  # Flow until a solid, or limit
  def flow(y = @y)
    #puts "Flowing Down: #{@y}, #{@x}"
    while !@sys[y+=1, @x] && y <= @sys.ymax do
      last = Tile.new(@sys, y, @x, :water)
    end; return last
  end
  # Flow Sideways
  def expand(section, c)
    section.push(self); return section \
      if solid? or !solid(@y+1, @x)
    (@sys[@y, @x-c] || Tile.new(@sys, @y, @x-c,
      :water)).expand(section, c)
  end
  # Tile Checks
  def solid(y, x)
    tile = @sys[y, x]
    tile.solid? if tile
  end
  def water?
    [:stable, :water].include? @type
  end
  def solid?
    [:stable, :clay].include? @type
  end
  # Yeet that pixel out
  def color(isActive = false)
    Color.from_rgb(isActive ? 240:30,
    solid? ? 240:30, water? ? 240:30)
  end
  def inspect
    @type
  end
end
# Ruby Apprently Doesn't Have Nested Classes
class System < Hash
  attr_accessor :ymax, :ymin, :xmax, :min, :stack
  def initialize(fname)
    File.readlines(fname).each do |vein|
      c,s,e = vein.scan(/\d+/).to_a.map(&:to_i)
      [*s..e].each &->(x){
        Tile.new self, *Array[x].send(if vein.ord.even?
          then 'append' else 'prepend' end, c), :clay
    } end; @ymin, @ymax = *self.keys.map(&:first).minmax
    @xmin, @xmax = *keys.map(&:last).minmax; @xmax += 1
    @stack = [Tile.new(self, 0, 500, :water)]; @xmin -= 1
    # Aids-donkey looping
    while head = @stack.shift do
      next unless last = head.flow
        while last = last.spill do end
    end; render
  end
  # Display Image
  def render(z = nil)
    image = Image.new(1 + @xmax - @xmin, 1 + @ymax - @ymin)
    (@ymin..@ymax).each do |y| (@xmin..@xmax). each do |x|
      tile = self[y, x]; image[x - @xmin, y - @ymin] \
        = tile.color(tile == z) if tile
    end end; image.save('debug.bmp', :bmp)
  end
  # Fuck Nested Arrays
  def []=(y, x, v)
    self.store([y,x], v)
  end
  def [](y, x)
    self.fetch([y,x], nil)
  end
  # Solution Functions
  def solve(*types)
    self.reduce 0, &->(s, ((y, x), t)) do
      if y >= @ymin && (types.include? \
        t.type) then 1 else 0 end + s
    end
  end
end
# Run Our Example System
testCase = System.new('test.txt')
raise "failed test" unless 57 ==
  testCase.solve(:water, :stable)
# Solver for Silver
solution = System.new('input.txt')
puts "Silver: #{solution.solve(:water, :stable)}"
puts "Gold: #{solution.solve(:stable)}"
