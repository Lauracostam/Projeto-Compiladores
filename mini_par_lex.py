#LEXER

from ply import lex
from ply.lex import TOKEN

# Reserved tokens

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'True': 'TRUE',
    'False': 'FALSE',
    'and': 'AND',
    'or': 'OR',
    'SEQ': 'SEQ',
    'PAR': 'PAR',
    'print' : "PRINT"
}

# List of token names.   This is always required

tokens = [
     'INT', 'FLOAT32', 'ID', 'LPAREN', 'RPAREN', 'BOOLEAN', 'COLON', 'SEMICOLON',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'NUMBER', 'EQUALS', 'LESSTHAN', 'GREATERTHAN',
    'NOTEQUAL', 'STRING', 'ERR_STRING', 'RCOMMA', 'COMMENT','GREATEQ', 'LESSEQ', 'EQUAL' ] + list(reserved.values())

# Regular expression rules for simple tokens

t_SEQ = r'SEQ'
t_PAR = r'PAR'
t_INT = r'int'
t_FLOAT32 = r'float32'
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_LPAREN = r'\('
t_RPAREN = r'\)'
#t_BOOLEAN = r'True|False'
t_COLON = r':'
t_SEMICOLON = r';'
t_RCOMMA = r'\"'
t_EQUALS = r'\='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LESSTHAN = r'\<'
t_GREATERTHAN = r'\>'
t_NOTEQUAL = r'\!\='
t_GREATEQ = r'\>\='
t_LESSEQ = r'\<\='
t_EQUAL   = r'\=\='
t_AND = r'and'
t_OR = r'or'
t_COMMENT = r'\#.*'


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_STRING(t):
    r'("[^"]*")'
    return t 

def t_ERR_STRING(t):
    r'"[^("|\n?)]*'
    return t 

def t_BOOLEAN(t): 
    r'True|False'
    t.type = 'BOOLEAN'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
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

#teste
data = "SEQ if (True) a = 5; else b = 10;"

lexer.input(data)

for tok in lexer:
    print(tok)
