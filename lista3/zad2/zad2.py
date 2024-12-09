import ply.yacc as yacc
import ply.lex as lex
from sys import stdin
from lex import *
from GF import *

def print_(*x) -> None:
    print(*x, end='')
    
lex.lex()

error_message = ""
RPN = ""
P = 1234577

precedence = (
    ("left", 'PLUS', 'MINUS'),
    ("left", 'MULTIPLY', 'DIVIDE'),
    ("right", 'POWER') )
   
def p_error(p):
    global RPN
    global error_message
    if error_message == "":
        error_message = "zła składnia"
    print("Błąd: " + error_message + "\n")
    RPN = ""
    error_message = ""
    
def p_start(p):
    """start : expression"""
    global RPN
    print(RPN)
    print('= ', p[1], '\n')
    RPN = ""
    error_message = ""
    
def p_start_com(p):
    """start : COMMENT"""
    pass
    
def p_expression_number(p):
    """expression : NUM"""
    global RPN 
    RPN += str(to_GF(p[1], P)) + ' '
    p[0] = to_GF(p[1],P)
    
def p_expression_neg(p):
    """expression : MINUS NUM"""
    global RPN
    global P
    RPN += str(to_GF(-p[2], P)) + ' '; 
    p[0] = to_GF(-p[2], P)
    
def p_expression_bracket(p):
    """expression : BRACKET_OPEN expression BRACKET_CLOSE"""
    p[0] = p[2]

def p_expression_plus(p):
    """expression : expression PLUS expression"""
    global RPN 
    global P
    RPN += '+ '; 
    p[0] = to_GF(p[1] + p[3], P);
    
def p_expression_minus(p):
    """expression : expression MINUS expression"""
    global RPN
    global P 
    RPN += '- '; 
    p[0] = to_GF(p[1] - p[3],P);
    
def p_expression_multiply(p):
    """expression : expression MULTIPLY expression"""
    global RPN 
    global P
    RPN += '* '; 
    p[0] = to_GF(p[1] * p[3],P);
    
def p_expression_divide(p):
    """expression : expression DIVIDE expression"""
    global RPN
    global P
    RPN += '/ '
    if(p[3] == 0):
    	error_message = str(p[3])+" nie posiada odwrotności w GF(" + str(P) + ")"
    	return
    p[0] = to_GF(divide_GF(p[1], p[3], P), P)
 
def p_expression_power(p):
    """expression : expression POWER exponent"""
    global RPN 
    global P
    RPN += '^ ';
    p[0] = to_GF(power_GF(p[1], p[3], P), P)
    
def p_exponent_number(p):
    """exponent : NUM"""
    global RPN 
    RPN += str(to_GF(p[1], P-1)) + ' '
    p[0] = to_GF(p[1],P)


def p_exponent_neg_number(p):
    """exponent : MINUS NUM"""
    global RPN 
    RPN += str(to_GF(-p[2], P-1)) + ' '
    p[0] = to_GF(-p[2],P-1)

yacc.yacc()

acc = ''
for line in stdin:
    if line[-2] == '\\':
        acc += line[:-2]
    elif acc != '':
        acc += line
        yacc.parse(acc)
        acc = ''
    else:
        yacc.parse(line)
