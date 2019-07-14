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
    unless @space[[x,y]] || y > @y0 then
      @space[[x, y]] = :water
      @stack.unshift([x,y])
      self.flow(x, y+1)
    end
  end
  # Flow Sideways
  def expand(x, y, n = -1)
    #puts "X: #{x}, Y: #{y}, #{solid?(x, y+1)}"
    if solid?(x, y+1) then
      @stack.unshift([x,y])
      @space[[x,y]] = :water
      return solid?(x + n, y) ?
        [x, y] : expand(x + n, y, n)
    end; @stack.unshift([x,y]); nil
  end
  # Balance to Pools
  def settle
    @stack.each do |tile|
      @space[tile] = :stale
    end
  end
  # Check Solid
  def solid?(x,y)
    [:stale, :clay].include? @space[[x,y]]
  end
  # count_all
  def count
    self.cycle [[500, 0]]
    @space.reduce 0, &->(s, ((x, y), v)) do
      if y >= @y1 && [:stale, :water].include?(v)
        then 1 else 0 end + s
    end
  end
end

testCase = System.new('test.txt')
raise "failed test" unless
  testCase.count == 57
# Run it
solution = System.new('input.txt')
puts "Silver: #{solution.count}"
