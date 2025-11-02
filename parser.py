# parser.py
# This file is based on the structure in 7.2 parser.py of your tutorial [cite: 344]

import ply.yacc as yacc

# Get the token map from the lexer. This is required. [cite: 121, 348]
from lexer import tokens

# --- Parser Grammar Rules ---

# The top-level rule: a stylesheet is a list of rules
def p_stylesheet(p):
    '''stylesheet : rules
                  | empty'''
    p[0] = "Stylesheet" # This is optional, but good practice

def p_rules(p):
    '''rules : rule
             | rules rule'''

# A single CSS rule: selector_list { declaration_list }
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
                        | empty''' # Allows for empty rule blocks like {}

# --- Helper Rules ---

# A single declaration (e.g., color: red;)
def p_declaration(p):
    'declaration : IDENTIFIER COLON value SEMICOLON'

# A rule for what a "value" can be
def p_value(p):
    '''value : IDENTIFIER
             | HEXCOLOR
             | NUMBER
             | NUMBER UNITS'''

# Rule for empty productions (used in declaration_list)
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors [cite: 126, 355]
def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}' (type: {p.type})")
    else:
        print("Syntax error at end of input")

# Build the parser [cite: 129, 359]
parser = yacc.yacc()