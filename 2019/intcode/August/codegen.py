class Block:
    def __init__(s):
        s.Body = []

class Program(Block):
    def Start(s):
        return [
            "rbx, !halt",
            "mul, !halt, 1, *1",
            "0_jmp, 0, !main"
        ]
    def End(s):
        return [
            "-global, 0, halt",
            "halt"]
    def Generate(s):
        Array = s.Start()
        for Term in s.Body:
            Array += Term.Generate()
        Array += s.End()
        return Array

class Function(Block):
    def Start(s):
        return [
    f"-global, 0, {s.Name}",
    f"-vars, " + ", ".join(s.Stack),
    f"rbx, {s.Size}"]

A = Program()
print(A.Generate())
