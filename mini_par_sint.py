import ply.yacc as yacc
from mini_par_lex import tokens    

def p_programa_minipar(p):
    'programa_minipar : bloco_stmt'
    p[0] = p[1]    
     
def p_bloco_stmt_stmts(p):
    '''bloco_stmt : stmts''' 
    p[0] = p[1] 
   
def p_stmts_stmt(p):
    '''stmts : stmt'''
    p[0] = p[1]
             
def p_stmts_stmts_stmt(p):
    '''stmts : stmts stmt'''
    p[0] = p[1]    

def p_stmt_expression(p):
    '''stmt : expression'''
    p[0] = p[1]
    
def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
        term      : term TIMES factor
                  | term DIVIDE factor'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

'''def p_term(p):
    term : term TIMES factor
            | term DIVIDE factor
    if p[2] == '':
        p[0] = p[1] p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]'''

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc(method='SLR')

def run(data):
    result = parser.parse(data)
    return result


