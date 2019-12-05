class Machine
  XVS = File.read('input.txt')
    .split(',').map(&:to_i)
  def initialize()
    @xvs, @idx = XVS.clone, 0
  end
  def execute
    op = @xvs[@idx].to_s.rjust(4, '0').chars
    op_code, @im = op.pop(2).join.to_i,
      op.reverse.map{|x| x == '1'}
    p1, p2, p3 = @params = @xvs[@idx+1, 3]
    case op_code
    when 99
      return @cout
    when 8
      @xvs[p3] = pts(1) ==
        pts(2) ? 1 : 0; @idx += 4
    when 7
      @xvs[p3] = pts(1) <
        pts(2) ? 1 : 0; @idx += 4
    when 6
      @idx = pts(1).zero? ?
        pts(2) : @idx + 3
    when 5
      @idx = pts(1).zero? ?
        @idx + 3 : pts(2)
    when 4
      @cout << pts(1); @idx += 2
    when 3
      @xvs[p1] = @cin.shift; @idx += 2
    when 2
      @xvs[p3] = pts(1) * pts(2); @idx += 4
    when 1
      @xvs[p3] = pts(1) + pts(2); @idx += 4
    end; false
  end
  def program(*cin)
    @cin, @cout = cin, []
    loop do value = execute
      return value.last if value
    end
  end
  def pts(i)
    v = @params[i -= 1]
    @im[i] ? v : @xvs[v]
  end
end

puts "Silver: #{Machine.new.program(1)}",
  "Gold: #{Machine.new.program(5)}"
