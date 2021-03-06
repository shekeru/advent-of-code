class Machine
  XVS = File.read('ins.txt')
    .split(',').map(&:to_i)
  def initialize(md = nil)
    @rbx, @cin, @cout = 0, [], []
    @xvs, @idx, @mode = XVS.clone, 0, md
    @cin << @mode if @mode.is_a? Numeric
  end
  def execute
    op = @xvs[@idx].to_s.rjust(5, '0').chars
    op_code, @im = op.pop(2).join.to_i,
      op.reverse.map(&:to_i)
    @params = @xvs[@idx+1, 3]
      case op_code
    when 9
      @rbx += pts(1); @idx += 2
    when 8
      inst(3) {pts(1) == pts(2) ? 1:0}
    when 7
      inst(3) {pts(1) < pts(2) ? 1:0}
    when 6
      @idx = pts(1).zero? ?
        pts(2) : @idx + 3
    when 5
      @idx = pts(1).zero? ?
        @idx + 3 : pts(2)
    when 4
      @cout << pts(1); @idx += 2
    when 3
      inst(1) {@cin.shift}
    when 2
      inst(3) {pts(1) * pts(2)}
    when 1
      inst(3) {pts(1) + pts(2)}
    else return
  end end
  def program(*cin)
    @cin += cin; while execute
      break if @mode && !@cout.empty?
    end; @cout.pop
  end
  def inst(i)
    @xvs[pts(i, ?o)] = yield
    @idx += i + 1
  end
  def pts(i, set = nil)
    v = @params[i -= 1]
    case @im[i]
    when 2; v += @rbx
      set ? v: @xvs[v]
    when 0; set ? v:
      @xvs[v]; else; v
  end.to_i end
  def end?
    99 == @xvs[@idx]
  end
end
# Shit Fucking Sucks
def paint(init = true)
  turtle, ptr = Machine.new(init), 0
  coords, tile = [0, 0], (Hash.new 0)
  while (value = turtle.program tile[coords]) do
    ptr += turtle.program >0 ? -1:1
    tile[coords.dup] = value; case (ptr %= 4)
      when 0; coords[0] -= 1; when 1; coords[1] -= 1
      when 2; coords[0] += 1; when 3; coords[1] += 1
end end; tile end; plate = paint(1)
# Fucking Autism Text
puts "Silver: #{paint.size}"
Y, X = plate.keys.map(&:first).uniq,
  plate.keys.map(&:last).uniq
Y.sort.each do |y| X.sort.each do |x|
  putc plate[[y, x]] >0 ? '#':' '
end; putc "\n" end
