# Linked Cups
class Node:
    def __init__(s, Value):
        s.Next, s.Prev = None, None
        s.Value = Value
    def __repr__(s, Str = ''):
        Str += str((X := s).Value)
        while X.Next is not s:
            Str += str((X := X.Next).Value)
        return Str #f"{s.Prev.Value} - ({s.Value}) - {s.Next.Value}\n"
    def Iter(St, V = 3):
        yield St.Next
        if V:
            yield from St.Next.Iter(V - 1)
    def Step(Cur):
        # Find Span
        *Three, Last = Cur.Iter()
        # Remove from Chain
        Cur.Next = Last
        Last.Prev = Cur
        # Find Index
        Where = Find(Cur.Value, Three)
        After = Where.Next
        # Insert Three
        Three[0].Prev = Where
        Where.Next = Three[0]
        Three[-1].Next = After
        After.Prev = Three[-1]
        # New Cup
        return Cur.Next
# Helper Functions
def Cycles(Count):
    global Cur, Index, Wrap
    Index = {N: Node(N) for N in Load}
    for A, B in zip(Load, Load[1:]+Load[0:]):
        Index[A].Next = Index[B]
        Index[B].Prev = Index[A]
    Cur, Wrap = Index[Load[0]], max(Load)
    for _ in range(Count):
        Cur = Cur.Step()
def Find(Dest, Opts):
    Dest = Dest - 1
    if not Dest:
        Dest = Wrap
    for X in Opts:
        if X.Value == Dest:
            return Find(Dest, Opts)
    return Index[Dest]
# Part 1
Load = [*map(int, '963275481')]
Cycles(100); print("Silver:",
    repr(Index[1])[1:])
# Part 2
Load += range(10, 1000001)
Cycles(10000000); print("Gold:",
    (F := Index[1].Next).Value
* F.Next.Value)
