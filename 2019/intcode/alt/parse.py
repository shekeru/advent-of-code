from lark import Lark

parser = Lark(r"""
    start: _NL* function+
    function: "[" args "]" "->" fname "(" locals ")" _NL section+ _NL*
    section: ctrl_label? asm_line*
    ctrl_label: /_[A-Z]\w+/ _NL
    ctr_ref: /_[A-Z]\w+/
    mem_slot: "#" /[a-z]\w*/
    mem_ref: "&" /([a-z]\w*)/
    term: /[^\s\&\[_;]+/
    literal: NUMBER
    string: STRING
    asm_line: term (literal | string | ctr_ref | mem_slot | mem_ref | term)+ _NL
    fname: NAME
    locals: NAME*
    args: NAME*
    %import common.CNAME -> NAME
    %import common.NEWLINE -> _NL
    %import common.SIGNED_INT -> NUMBER
    %import common.ESCAPED_STRING -> STRING
    %import common.WS_INLINE
    %ignore WS_INLINE
    COMMENT: ";" /[^\n]/*
    %ignore COMMENT
""", parser="earley")

def Parse(fname):
    return parser.parse(
        open(f'code/{fname}.ic1')
    .read())
