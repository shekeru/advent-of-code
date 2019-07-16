require 'imageruby'
include ImageRuby

class Tile
  def initialize(z, y, x, t = :clay)
    @type, z[y, x] = t, self
  end
  # Yeet that type out
  def inspect
    @type
  end
end

class System < Hash
  attr_accessor :ymax, :ymin, :xmax, :min
  def initialize(fname)
    File.readlines(fname).each do |vein|
      c,s,e = vein.scan(/\d+/).to_a.map(&:to_i)
      [*s..e].each &->(x){
        Tile.new self, *Array[x].send(if vein.ord.even?
          then 'append' else 'prepend' end, c)
    } end
    ys, xs = self.keys.map(&:first), self.keys.map(&:last)
    @ymin, @ymax, @xmin, @xmax = *ys.minmax, *xs.minmax
    end
    # Display Image
    def render
      image = Image.new(1 + @xmax - @xmin, 1 + @ymax - @ymin)
      (@ymin..@ymax).each do |y| (@xmin..@xmax). each do |x|
        image[x - @xmin, y - @ymin] = Color.from_rgb(40, 40, 40)
      end; end; image.save('debug.bmp', :bmp)
    end
    # Fuck Nested Arrays
    def []=(y, x, v)
      self.store([y,x], v)
    end
    def [](y, x)
      self.fetch([y,x])
    end
end


testCase = System.new('test.txt')
testCase.render
