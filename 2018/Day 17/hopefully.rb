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
  end
  def cycle(flows)
    @stack.clear; ys = []; puts flows
    flows.each &->(xs){flow(*xs)}
    (@stack.dup).each do |tile| @stack.clear
      [expand(*tile, 1), expand(*tile)
      ].all? ? self.settle : (ys.push *@stack)
    end; puts @space
    cycle ys if !ys.empty?
  end
  # Flow Down
  def flow(x, y)
    unless @space[[x,y]] then
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
end

sys = System.new('test.txt')
sys.cycle [[500, 1]]
puts sys.space
