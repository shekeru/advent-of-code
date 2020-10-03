class Program:
    def __init__(s, xvs):
        s.Idx, s.Rbx = 0, 0
        s.Tape = xvs.copy()
        s.Inputs = []
    def Push(s, Value):
        s.Inputs.append(Value)
    def NextOpCode(s):
        Code = str(s.Tape[s.Idx]).rjust(5, '0')
        s.Mode = (*map(int, Code[:-2][::-1]),)
        return getattr(s, '_' + Code[-2:])()
    def Eval(s):
        Value = True
        while Value != False:
            if Value := s.NextOpCode():
                yield Value
    def __getitem__(s, x):
        Value = s.Tape[s.Idx + x]
        if not(Type := s.Mode[x - 1]):
            return s.Tape[Value]
        if Type == 1:
            return Value
        if Type == 2:
            return s.Tape[s.Rbx + Value]
    def __setitem__(s, x, v):
        Value = s.Tape[s.Idx + x]
        if not(Type := s.Mode[x - 1]):
            s.Tape[Value] = v
        if Type == 1:
            s.Tape[s.Idx + x] = v
        if Type == 2:
            s.Tape[s.Rbx + Value] = v
    def _01(s):
        s[3] = s[1] + s[2]
        s.Idx += 4
    def _02(s):
        s[3] = s[1] * s[2]
        s.Idx += 4
    def _04(s):
        V = s[1]
        s.Idx += 2
        return V
    def _99(s):
        return False
print([*Program([21101, 55, 55, 0, 4, 0, 99]).Eval()])
