# parser.py

import ply.yacc as yacc
from lexer import tokens

# --- Global Error Flag ---
PARSE_ERROR_FLAG = False
# -------------------------

# The top-level rule: a stylesheet is a list of rules
def p_stylesheet(p):
    '''stylesheet : rules
                  | empty'''
    p[0] = "Stylesheet"

def p_rules(p):
    '''rules : rule
             | rules rule'''

def p_rule(p):
    'rule : selector_list LBRACE declaration_list RBRACE'

# --- Your 5 Constructs ---

# 1. Element, 3. ID, 4. Class Selector
def p_selector(p):
    '''selector : IDENTIFIER
                | ID_SELECTOR
                | CLASS_SELECTOR'''

# 2. Group Selector (e.g., h1, .class, #id)
def p_selector_list(p):
    '''selector_list : selector
                     | selector_list COMMA selector'''

# 5. Rule with Multiple Declarations
def p_declaration_list(p):
    '''declaration_list : declaration
                        | declaration_list declaration
                        | empty'''

# --- Helper Rules ---

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

# --- Error Rule ---
def p_error(p):
    global PARSE_ERROR_FLAG
    PARSE_ERROR_FLAG = True  # Set the flag to True when an error occurs
    
    if p:
        print(f"Syntax error at token '{p.value}' (type: {p.type})")
    else:
        print("Syntax error at end of input")

# Build the parser
parser = yacc.yacc()