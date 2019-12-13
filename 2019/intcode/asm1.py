def op(code, x = 0, y = 0, z = 0):
    im = "".join(map(str, [z, y, x]))
    return im.lstrip('0') + '0' + str(code)
# Intcode Program
class Heap:
    def __init__(h, s, d):
        h.start, h.size = s.rbx, len(d)
        s.function([op(9, 1), h.start])
        h.reset = lambda: s.function \
            ([op(9, 1), h.size - h.start])
class Function:
    def __init__(f, s, proc, ex):
        f.size = len(proc) + ex
    def set_heap(f, heap):
        f.heap = heap
        heap.reset()
        f.size += 4
        return f
    def __add__(f, g):
        return f.size + g.size
class Assembly:
    def __init__(s):
        s.program = [op(9, 1), 2]
        s.rbx, s.text = 0, [99]
    def generate(s):
        return ",".join(map(str, s.program + s.text))
    def function(s, proc, ex = 0):
        s.program += proc
        s.program[1] += len(proc)
        return Function(s, proc, ex)
    def emplace(s, data):
        s.rbx += len(data)
        s.text += data[::-1]
        return Heap(s, data)
    def get_idx(s):
        return len(s.program)
# Implementation Shit
    def impl_print(s, text, sep = "\n"):
        heap = s.emplace([*map(ord, text+sep)])
        body = s.function([
            op(9, 1), -1, # rbx++
            op(4, 2), 1 # putc, rbx(1)
        ]); body = s.impl_for(heap.size, body.size)
        return body.set_heap(heap)
    def impl_for(s, n, jmp = 0):
        idx = s.get_idx()
        return s.function([
            op(1, 1, 1), -1, n, idx+2, #decrement
            op(5, y = 1), idx+2, idx-jmp, #loop index
            op(1, y = 1), idx+2, n, idx+2,
        ], jmp)
    def impl_mod(s, heap, n):
        idx = s.get_idx() + 2
        body = s.function([
            op(9, 1), -1, # rbx--
            op(1, 2, 1, 2), 1, -n, 1, # rbx(1) % n
            op(7, 2, 1), 1, 0, idx + 9,
            op(6, 1, 1), 0, idx,
            op(2, 2, 1, 2), 1, -1, 1,
        ]); return body.set_heap(heap)
# User Space
    def user_test(s):
        # Label:
        s.impl_print("--Before--")
        # Label: A
        A1 = s.impl_print("\t Line One")
        A2 = s.impl_print("\t Line Two")
        params = s.emplace([0])
        s.function([op(1, 1, 1), ])
        A3 = s.impl_mod(params, 3)
        # forI = s.get_idx() + 2
        # A += = s.function([
        #     op(1, 1, 1,
        # ]);
        fA = s.impl_for(3, A1 + A2 + A3.size)
        # Label: B
        B = s.impl_print("--After--")
        fB = s.impl_for(2, fA+B)
        # Label: C
        s.impl_print("Done!")
# Dogshit.jpg
asm = Assembly()
asm.user_test()
print(asm.generate())
