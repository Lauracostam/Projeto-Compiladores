import ply.yacc as yacc
from lexer import tokens  

precedence = (
    ('left', 'IF', 'ELSE'),
    ('left', 'WHILE'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
)      
            
ids = { }

def p_programa_minipar(p):
    'programa_minipar : bloco_stmt' 
    
def p_bloco_stmt_bloco(p):
    '''bloco_stmt : stmts'''     
    p[0] = p[1] 

def p_stmts_stmt(p):
    '''stmts : stmt'''   
    p[0] = p[1]
             
def p_stmts_stmts_stmt(p):
    '''stmts : stmts stmt'''
    p[0] = p[1]    
    
def p_statement_assign(p):
    'stmt : ID EQUALS expression'
    ids[p[1]] = p[3]
    
def p_statement_expr(p):
    'stmt : expression'
    #print(p[1])

def p_stmt_comparison(p):
    'stmt : comparison'
    p[0] = p[1]

def p_stmt_if(p):
    '''stmt : IF LPAREN BOOLEAN RPAREN stmt %prec IF
            | IF LPAREN comparison RPAREN stmt %prec IF'''
    if p[3] == True:  # p[3] contém o valor booleano da condição
        p[0] = p[5]
    else:
        p[0] = None
    

def p_stmt_if_else(p):
    '''stmt : IF LPAREN BOOLEAN RPAREN stmt ELSE stmt %prec IF
            | IF LPAREN comparison RPAREN stmt ELSE stmt %prec IF'''
    if p[3]:  # p[3] contém o valor booleano da condição
        p[0] = p[5]
    else:
        p[0] = p[7]

def p_stmt_while(p):
    '''stmt : WHILE LPAREN BOOLEAN RPAREN stmt %prec WHILE
            | WHILE LPAREN comparison RPAREN stmt %prec WHILE'''
    while p[3]:  # p[3] contém o valor booleano da condição
        p[0] = p[5]
def p_comparison(p):
    '''comparison : expression EQUAL expression
               | expression NOTEQUAL expression
               | expression GREATERTHAN expression
               | expression LESSTHAN expression
               | expression GREATEQ expression
               | expression LESSEQ expression'''
                  
    if p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
        
def p_expression(p):
    '''expression : expression PLUS expression
                    | expression MINUS expression
                    | expression TIMES expression
                    | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

'''def p_term(p):
    term : term TIMES factor
            | term DIVIDE factor
    if p[2] == '':
        p[0] = p[1] p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]'''

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]
    
def p_statement_print(p):
    'stmt : PRINT LPAREN expression RPAREN'
    print(p[3])
    
def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_name(p):
    'expression : ID'
    try:
        p[0] = ids[p[1]]
    except LookupError:
        print(f"Undefined id {p[1]!r}")
        p[0] = 0
def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc(method='SLR')
input_test = '''a = 2
b = 3
if(a > b) print(a)
'''

input_test = '''a = 7
b = a * 2
print(a + b)
if(a < b) print(a)
'''
result = parser.parse(input_test)

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)

#isso aqui só roda se o server chamar com a tag PAR
# é pra fazer isso no server, quando identificar PAR
'''thread1 = threading.Thread(target = alguma coisa,)
thread2 = threading.Thread(target = alguma coisa)


thread1.start()
thread2.start()'''