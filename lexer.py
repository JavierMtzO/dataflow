import ply.lex as lex
# Reserved words
reserved = {
    'program': 'PROG',
    'var': 'VAR',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'void': 'VOID',
    'func': 'FUNC',
    'main': 'MAIN',
    'if': 'IF',
    'else': 'ELSE',
    'return': 'RETURN',
    'print': 'PRINT',
    'for': 'FOR',
    'to': 'TO',
    'do': 'DO',
    'while': 'WHILE',
    'true': 'TRUE',
    'false': 'FALSE',
    'dataframe': 'DATAFRAME',
    'describe':'DESCRIBE',
    'title': 'TITLE'
}

tokens = (
    'DIFFERENT', 'EQUAL', 'AND', 'OR', 'EMPTY', 'I_CONST', 'F_CONST', 'C_CONST', 'ID'
)   + tuple(reserved.values())

# literal symbols
literals = [';', ',', '.', '{', '}', '(', ')', '[', ']', '=', '+', '-', '*', '/', '>', '<']


# Token regular expressions
t_DIFFERENT = r'\!\='
t_EQUAL = r'\=\='
t_AND = r'\&\&'
t_OR = r'\|\|'
t_EMPTY = r'\bε\b'

#  Complex tokens

def t_I_CONST(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

def t_F_CONST(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_C_CONST(t):
    r'\'[0-9A-Za-z_ ]{1}\''
    t.value = list(t.value)[1]
    return t

def t_ID(t):
    r'[A-Za-z]([A-Za-z] | [0-9] | \_)*'
    if t.value not in reserved:
        t.type = 'ID'
    else:
        t.type = reserved[t.value]
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

################  TEST  ################
# data = '''
# for counter = 65 to 67 do { counter = counter + 1 }
# '''

# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break 
#     print(tok)

#############################################