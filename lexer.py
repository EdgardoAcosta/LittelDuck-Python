import ply.lex as lex

# Key words
keywords = {
    'program': 'PROGRAM',
    'print': 'PRINT',
    'if': 'IF',
    'else': 'ELSE',
    'var': 'VAR',
    'int': 'INT',
    'float': 'FLOAT',

}

# Tokens based on the parser

tokens = ['SEMICOLON', 'LEFTBRACKET', 'RIGHTBRACKET', 'GREATER', 'LESS', 'NOTEQUAL', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
          'LEFTPAREN', 'RIGHTPAREN', 'ID', 'CTEI', 'CTEF', 'COLON', 'EQUALS', 'CTESTRING', 'COMMA'] + list(
    keywords.values())

# Regular expressions

t_SEMICOLON = r';'
t_LEFTBRACKET = r'\{'
t_RIGHTBRACKET = r'\}'
t_GREATER = r'>'
t_LESS = r'<'
t_NOTEQUAL = r'<>'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LEFTPAREN = r'\('
t_RIGHTPAREN = r'\)'
t_COLON = r':'
t_EQUALS = r'\='
t_CTESTRING = r'\".*\"'
t_COMMA = r'\,'
t_ignore = " \t"


# Regular expression with some action

# Define a ID
def t_ID(t):
    r'[A-za-z]([A-za-z]|[0-9])*'
    t.type = keywords.get(t.value, 'ID')
    return t


# Define a variable int
def t_CTEI(t):
    r'\d+'
    t.value = int(t.value)


# Define a float number
def t_CTEF(t):
    r'([0-9]*\.[0-9]+|[0-9]+)'
    t.value = float(t.value)


# Define a new line or multiple new lines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Define a comment
def t_comment(t):
    r'\//.*'
    pass


def t_error(t):
    print("Lexical error ' {0} ' found in line ' {1} ' ".format(t.value[0], t.lineno))
    t.lexer.skip(1)


lex.lex()
