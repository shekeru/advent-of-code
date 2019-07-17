# Fuck you ruby
RubyVM::DEFAULT_PARAMS = {
  thread_vm_stack_size: 1048576^2,
}
require 'imageruby'
include ImageRuby
# Helper Class
class Tile
  attr_accessor :type
  def initialize(sys, y, x, t = nil)
    @type, sys[y, x] = t, self
    @sys, @y, @x, = sys, y, x
  end
  # Flow Down
  def flow(iters = nil)
      return if @y >= @sys.ymax
    puts "Current tile: #{@y}, #{@x}"
    if @type == :water then
      unless @sys[@y+1, @x] then
        return { Tile.new(@sys, @y+1, @x, :water).flow(@y) }
      else
          return if @y == iters # Fuck everything else
        layer = [*@sys[@y, @x].expand([], -1).reverse,
          *@sys[@y, @x].expand([], 1).drop(1)]
        if layer[0].solid? and layer[-1].solid? then
          layer[1..-2].each &->(tile) {
            tile.type = :stable
          }; layer[1..-2].each(&:update)
        else layer[0].flow(@y); layer[-1].flow(@y)
        end
      end
    end
    #@sys.render(@y); #gets
  end
  # Flow Sideways
  def expand(section, c)
    section.push(self); return section \
      if solid? or !solid(@y+1, @x)
    (@sys[@y, @x-c] || Tile.new(@sys, @y, @x-c,
      :water)).expand(section, c)
  end
  # Upwards Updates
  def update
   @sys[@y - 1, @x].flow(@y) if @sys[@y - 1, @x]
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
  # Yeet that type out
  def color(isActive = false)
    isActive = isActive ? 240:30
    isSolid = self.solid? ? 240:30
    isWater = self.water? ? 240:30
    Color.from_rgb(isActive, isSolid, isWater)
  end
  def inspect
    @type
  end
end
# Ruby Apprently Doesn't Have Nested Classes
class System < Hash
  attr_accessor :ymax, :ymin, :xmax, :min
  def initialize(fname)
    File.readlines(fname).each do |vein|
      c,s,e = vein.scan(/\d+/).to_a.map(&:to_i)
      [*s..e].each &->(x){
        Tile.new self, *Array[x].send(if vein.ord.even?
          then 'append' else 'prepend' end, c), :clay
    } end
    ys, xs = self.keys.map(&:first), self.keys.map(&:last)
    @ymin, @ymax, @xmin, @xmax = *ys.minmax, *xs.minmax
      Fn = Tile.new(self, 0, 500, :water).flow # Spawn Spring
      while Fn = yield Fn do end
    end
    # Display Image
    def render(z = nil)
      image = Image.new(1 + @xmax - @xmin, 1 + @ymax - @ymin)
      (@ymin..@ymax).each do |y| (@xmin..@xmax). each do |x|
        if tile = self[y, x] then
          image[x - @xmin, y - @ymin] = tile.color(y == z)
      end end end; image.save('debug.bmp', :bmp)
    end
    # Fuck Nested Arrays
    def []=(y, x, v)
      self.store([y,x], v)
    end
    def [](y, x)
      self.fetch([y,x], nil)
    end
    # Solution Functions
    def silver
      self.reduce 0, &->(s, ((y, x), t)) do
        if y >= @ymin && t.water?
          then 1 else 0 end + s
      end
    end
end
# Run Our Example System
testCase = System.new('test.txt')
puts testCase
raise "failed test" unless
  testCase.silver == 57
# Solver for Silver
#solution = System.new('test.txt')
#puts "Silver: #{solution.count}"
#solution.render
