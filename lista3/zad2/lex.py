import ply.lex as lex

tokens = (
	'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'POWER', 'BRACKET_OPEN', 'BRACKET_CLOSE', 'NUM', 'COMMENT'
)

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_POWER = r'\^'
t_BRACKET_OPEN = r'\('
t_BRACKET_CLOSE =  r'\)'
t_COMMENT = r'\#.*'

def t_NUM(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t
    
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print(f'\nBłąd: niepoprawny znak {t.value[0]!r}')
    t.lexer.skip(1)
 
lexer = lex.lex()
