Tape = File.read("input.txt").scan(/(\w+) ([-+]\d+)/).map{[_1, _2.to_i]}
# Simulation
def eval
  acc = ix = 0; seen = {}
  while ix < Tape.size do
    return acc if seen[ix]; seen[ix] = 1
    case Tape[ix][0]
      when "acc"
        acc += Tape[ix][1]
      when "jmp"
        ix += Tape[ix][1] - 1
    end; ix += 1
  end; return -acc
end; puts "Silver: #{eval}"
# Correction
def unhalt
  Tape.map.with_index do |(x, c), i|
    Tape[i][0] = case x
      when "nop"; "jmp"
      when "jmp"; "nop"
      else x
    end; eval.then do
      return -_1 if _1 < 0
    end; Tape[i][0] = x
end; end; puts "Gold: #{unhalt}"
