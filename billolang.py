# calclex.py

from sly import Lexer
from sly import Parser

class CalcLexer(Lexer):
    # Set of token names.   This is always required
    tokens = { NUMBER, ID, WHILE, FOR, IF, ELSE, PRINT, VAR,
               PLUS, MINUS, TIMES, DIVIDE, ASSIGN,
               EQ, LT, LE, GT, GE, NE, ARROW, ARROWL }


    literals = { '(', ')'}

    # String containing ignored characters
    ignore = ' \t'

    # Regular expression rules for tokens
    ARROW   = r'->'
    ARROWL  = r'-->'
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    EQ      = r'=='
    ASSIGN  = r'='
    LE      = r'<='
    LT      = r'<'
    GE      = r'>='
    GT      = r'>'
    NE      = r'!='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    # Identifiers and keywords
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if'] = IF
    ID['else'] = ELSE
    ID['while'] = WHILE
    ID['for'] = FOR
    ID['print'] = PRINT
    ID['var'] = VAR

    ignore_comment = r'\#.*'

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1


class CalcParser(Parser):
    # Get the token list from the lexer (required)
    tokens = CalcLexer.tokens

    # Grammar rules and actions
    @_('expr PLUS term')
    def expr(self, p):
        return p.expr + p.term

    @_('expr MINUS term')
    def expr(self, p):
        return p.expr - p.term

    @_('term')
    def expr(self, p):
        return p.term

    @_('term TIMES factor')
    def term(self, p):
        return p.term * p.factor

    @_('term DIVIDE factor')
    def term(self, p):
        return p.term / p.factor

    @_('factor')
    def term(self, p):
        return p.factor

    @_('NUMBER')
    def factor(self, p):
        return p.NUMBER

    @_('LPAREN expr RPAREN')
    def factor(self, p):
        return p.expr

if __name__ == '__main__':
    data = '''# Counting
var x ->
= x 0 ->
( while < x 10 -->
    print x ->
    = x (+ x 1) ->
)
'''
    lexer = CalcLexer()
    token = lexer.tokenize(data)

    for tok in token:
        print(tok)
    
    parser = CalcParser()
    print(parser.parse(token))
