from rply import LexerGenerator

class Lexer(LexerGenerator):
    def __init__(sl):
        super().__init__()
        # Print
        sl.add('PRINT', r'print')
        # Parenthesis
        sl.add('OPEN_PAREN', r'\(')
        sl.add('CLOSE_PAREN', r'\)')
        # Operators
        sl.add('ADD', r'\+')
        sl.add('MUL', r'\*')
        # Number
        sl.add('NUMBER', r'\d+')
        # Ignore spaces
        sl.ignore('\s+')
    def get_lexer(sl):
        return sl.build()
