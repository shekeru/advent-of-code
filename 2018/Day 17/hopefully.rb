require 'rubygems'
require 'imageruby'
include ImageRuby

class System
  attr_accessor :stack
  attr_accessor :space
  def initialize(fname)
    @space = Hash.new
    @stack = Array.new
    # Load Veins
    File.readlines(fname).each do |vein|
      c,s,e = vein.scan(/\d+/).to_a.map(&:to_i)
      [*s..e].each &->(x){
        @space[Array[x].send(vein.ord.odd? \
          ? 'append' : 'prepend', c)] = :clay
    }; end
    @y0 = @space.keys.max_by(&:last).last
    @y1 = @space.keys.min_by(&:last).last
    @x0 = @space.keys.max_by(&:first).first
    @x1 = @space.keys.min_by(&:first).first
  end
  def cycle(flows)
    @stack.clear; ys = []
    flows.each &->(xs){flow(*xs)}
    @stack.dup.each do |tile| @stack.clear
      [expand(*tile, 1), expand(*tile)
      ].all? ? self.settle : (ys.push *@stack)
    end; cycle ys if !ys.empty?
  end
  # Flow Down
  def flow(x, y)
    puts "#{x}, #{y}"
    unless solid?(x, y) || y > @y0 then
      @space[[x, y]] = :water
      @stack.unshift([x,y])
      self.flow(x, y+1)
    end
  end
  # Flow Sideways
  def expand(x, y, n = -1)
    if solid?(x, y+1) then
      @stack.unshift([x,y])
      @space[[x,y]] = :water
      return solid?(x + n, y) ?
        [x, y] : expand(x + n, y, n)
    end; @stack.unshift([x,y]); nil
  end
  # Balance to Pools
  def settle
    @stack.dup.each do |x, y|
      @space[[x, y]] = :stale
    end
  end
  # Check Solid
  def solid?(x,y)
    [:stale, :clay].include? @space[[x,y]]
  end
  def water?(x,y)
    [:stale, :water].include? @space[[x,y]]
  end
  # count_all
  def count
    self.cycle [[500, 0]]
    @space.reduce 0, &->(s, ((x, y), _)) do
      if y >= @y1 && water?(x, y)
        then 1 else 0 end + s
    end
  end
  # debug render
  def render
    image = Image.new(@x0 - @x1 + 1, @y0 - @y1 + 1)
    (@y1..@y0).each do |y| (@x1..@x0). each do |x|
      image[x-@x1,y-@y1] = Color.from_rgb(40, solid?(x, y) ?224:0, water?(x, y) ?224:0)
    end; end; image.save('debug.bmp', :bmp)
  end
end

testCase = System.new('test.txt')
raise "failed test" unless
  testCase.count == 57
# Run it
solution = System.new('test.txt')
puts "Silver: #{solution.count}"
solution.render
