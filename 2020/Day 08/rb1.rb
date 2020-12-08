Tape = File.read("input.txt").scan(/(\w+) ([-+]\d+)/).map{[_1, _2.to_i]}
# Simulation
def eval
  acc = ix = 0; seen = {}
  while ix < Tape.size do
    seen[ix] ? (return acc, false) : seen[ix] = 1
    case Tape[ix][0]
      when "acc"
        acc += Tape[ix][1]
      when "jmp"
        ix += Tape[ix][1] - 1
    end; ix += 1
  end; return acc, true
end; puts "Silver: #{eval[0]}"
# Correction
def unhalt
  Tape.map.with_index do |(x, c), i|
    Tape[i][0] = case x
      when "nop"; "jmp"
      when "jmp"; "nop"
      else x
    end; v, t = eval
      Tape[i][0] = x
    return v if t
end; end; puts "Gold: #{unhalt}"
