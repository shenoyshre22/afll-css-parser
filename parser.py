# parser.py

import ply.yacc as yacc
from lexer import tokens

# --- DELETE THE GLOBAL FLAG ---
# PARSE_ERROR_FLAG = False  <-- DELETE THIS

# --- ALL GRAMMAR RULES (p_stylesheet, p_rule, etc.) ARE UNCHANGED ---

def p_stylesheet(p):
    '''stylesheet : rules
                  | empty'''
    p[0] = "Stylesheet"

def p_rules(p):
    '''rules : rule
             | rules rule'''

def p_rule(p):
    'rule : selector_list LBRACE declaration_list RBRACE'

def p_selector(p):
    '''selector : IDENTIFIER
                | ID_SELECTOR
                | CLASS_SELECTOR'''

def p_selector_list(p):
    '''selector_list : selector
                     | selector_list COMMA selector'''

def p_declaration_list(p):
    '''declaration_list : declaration
                        | declaration_list declaration
                        | empty'''

def p_declaration(p):
    'declaration : IDENTIFIER COLON value SEMICOLON'

def p_value(p):
    '''value : IDENTIFIER
             | HEXCOLOR
             | NUMBER
             | NUMBER UNITS'''

def p_empty(p):
    'empty :'
    pass

# --- THIS FUNCTION IS UPDATED ---
def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}' (type: {p.type})")
        lexer_obj = p.lexer  # Get the lexer from the token
    else:
        print("Syntax error at end of input")
        lexer_obj = parser.lexer # Get the lexer from the parser object
    
    # Set the flag on the lexer instance
    lexer_obj.error_found = True

# Build the parser
parser = yacc.yacc()