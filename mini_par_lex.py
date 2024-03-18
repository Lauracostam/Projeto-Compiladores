import ply.lex as lex

# Palavras-chave reservadas
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'True': 'TRUE',
    'False': 'FALSE',
    'and': 'AND',
    'or': 'OR',
    'SEQ': 'SEQ',
    'PAR': 'PAR'
}

# Lista de tokens
tokens = [
    'ID', 'NUMBER', 'STRING', 'BOOLEAN',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LESSTHAN', 'GREATERTHAN', 'EQUAL', 'NOTEQUAL',
    'LPAREN', 'RPAREN', 'ASPAS', 'COMMENT', 'GREATEQ', 'LESSEQ'
] + list(reserved.values())

# Expressões regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_EQUAL = r'='
t_NOTEQUAL = r'!='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASPAS = r'\"'
t_COMMENT = r'\#.*'

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Tratamento de números inteiros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Tratamento de strings
def t_STRING(t):
    r'"[^"]*"'
    return t

# Tratamento de identificadores
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica palavras reservadas
    return t

# Tratamento de quebras de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erros
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construa o analisador léxico
lexer = lex.lex()

# Exemplo de teste
example_input = '''
SEQ
    result = True
    i = 1
    WHILE (i <= 10)
        IF (i>2 and i != 0 and result)
            result = result and False
        i = i + 1
    #testando comentarios
PAR
    j = 1
    WHILE (j <= 10)
        IF (j>2 and j != 0 and result)
            result = result and False
        j = j + 1
'''

lexer.input(example_input)

# Exiba os tokens encontrados
while True:
    tok = lexer.token()
    if not tok:
        break  # Não há mais entrada
    print(tok)
