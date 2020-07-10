class Machine
  def initialize(tape, md = nil)
    @cin, @cout, @mode = [], [], md
    @xvs, @idx, @rbx, = tape.clone, 0, 0
    @cin << @mode if @mode.is_a? Numeric
  end
  def execute
    op = @xvs[@idx].to_s.rjust(5, '0').chars
    op_code, @im = op.pop(2).join.to_i,
      op.reverse.map(&:to_i)
    @params = @xvs[@idx+1, 3]
    return if @rbx < 0
    puts "#{@xvs.take 18}"
    puts "op: #{op_code}, idx: #{@idx}, rbx: #{@rbx}, #{@params}"
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
      # puts pts(1)
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
    end; @mode == false ? @cout : @cout.pop
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
    # when 1; set ? : v;
    when 0; set ? v : 
      @xvs[v]; else; v
  end.to_i end
  def end?
    99 == @xvs[@idx]
  end
end
# Pattern Scan & Force Floor
xvs = File.read('ins.txt').split(',').map(&:to_i)
puts Machine.new(xvs, false).program.map{|x|
  [255, x].min.chr}.join
