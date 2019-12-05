xvs = File.read('2019/Day 05/input.txt')
  .split(',').map(&:to_i)

class Machine
  def initialize(xvs)
    @xvs, @idx = xvs.clone, 0
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
      @xvs[p3] = arg(1) ==
        arg(2) ? 1 : 0
      @idx += 4
    when 7
      @xvs[p3] = arg(1) <
        arg(2) ? 1 : 0
      @idx += 4
    when 6
      if arg(1).zero?
        @idx = arg(2)
      else
        @idx += 3
      end
    when 5
      unless arg(1).zero?
        @idx = arg(2)
      else
        @idx += 3
      end
    when 4
      @cout << arg(1)
      @idx += 2
    when 3
      @xvs[p1] = @cin.shift
      @idx += 2
    when 2
      @xvs[p3] = arg(1) * arg(2)
      @idx += 4
    when 1
      @xvs[p3] = arg(1) + arg(2)
      @idx += 4
    end; nil
  end
  def arg(i)
    v = @params[i -= 1]
    @im[i] ? v : @xvs[v]
  end
  def run_program(*cin)
    @cin, @cout = cin, []
    loop do value = execute
      return value.last if value
    end
  end
end

puts "Silver: #{Machine.new(xvs).run_program(1)}",
  "Gold: #{Machine.new(xvs).run_program(5)}"
