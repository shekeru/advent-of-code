from rply import LexerGenerator

class Lexer(LexerGenerator):
    def __init__(sl):
        super().__init__()
        # Parenthesis
        sl.add('OPEN', r'\(')
        sl.add('CLOSE', r'\)')
        # Compiler Terms
        sl.add("BYTES", r'bytes')
        sl.add("DEFN", r'defn')
        sl.add("LOOP", r'loop')
        sl.add("REF", r'&\w+')
        sl.add("PTR", r'\^\w+')
        # Assembly Terms
        sl.add("ADD", r'\+')
        sl.add("MUL", r'\*')
        sl.add("CIN", r'getc')
        sl.add("COUT", r'putc')
        sl.add("1_JMP", r'1j')
        sl.add("0_JMP", r'0j')
        sl.add("LT", r'<')
        sl.add("EQ", r'=')
        # Numbers & Vars
        sl.add("STRING", r'".*"')
        sl.add('NUMBER', r'-?\d+')
        sl.add('GLOBAL', r'[\$!]\w+')
        sl.add('TERM', r'~?\w+')
        # Ignore spaces
        sl.ignore('\s+')
ll = Lexer().build()

def Read(Tree, List):
    if len(List) == 0:
        print("end eof")
        return
    token = List.pop(0)
    if token.name == "OPEN":
        New = []; Tree.append(New)
        while List[0].name != "CLOSE":
            Read(New, List)
        List.pop(0)
    elif token.name == 'CLOSE':
        raise SyntaxError('unexpected )')
    else:
        Tree.append(token)

def Open(fn):
    ss = open(f"code/{fn}.ic").read()
    Tree, List = [], [*ll.lex(ss)]
    while List:
        Read(Tree, List)
    return Tree

ss = open(f"code/ex1.ic").read()
Tree, List = [], [*ll.lex(ss)]
