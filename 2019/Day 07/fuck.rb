class Machine
  XVS = File.read('input.txt')
    .split(',').map(&:to_i)
  def initialize(mode = nil)
    @cin, @cout = [], []
    @xvs, @idx, @mode =
      XVS.clone, 0, mode
    @cin << @mode if @mode
  end
  def execute
    op = @xvs[@idx].to_s.rjust(4, '0').chars
    op_code, @im = op.pop(2).join.to_i,
      op.reverse.map{|x| x == '1'}
    @params = @xvs[@idx+1, 3]
      case op_code
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
    @xvs[@params[i - 1]] =
      yield; @idx += i + 1
  end
  def pts(i)
    v = @params[i -= 1]
    @im[i] ? v : @xvs[v]
  end
  def end?
    99 == @xvs[@idx]
  end
end
# So easy, then so hard...
puts "Silver: " + (0..4).to_a.permutation.map{
  |xs| xs.reduce(0){|a, e|
    Machine.new.program(e, a)
}}.max.to_s
# Honestly, go fuck yourself Eric
puts "Gold: " + (5..9).to_a.permutation.map{
  |xs| st, v, i = xs.map{|x|
    Machine.new x}, 0, 0
  while !st[i].end? do
    v = st[i].program(v)
    i = (i + 1) % 5 end
v}.max.to_s
