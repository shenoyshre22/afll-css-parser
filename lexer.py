# lexer.py

import ply.lex as lex

# List of token names (NO CHANGE)
tokens = (
    'IDENTIFIER', 'ID_SELECTOR', 'CLASS_SELECTOR', 'NUMBER', 'UNITS',
    'HEXCOLOR', 'LBRACE', 'RBRACE', 'COMMA', 'COLON', 'SEMICOLON',
)

# Simple Token Rules (NO CHANGE)
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_COMMA     = r','
t_COLON     = r':'
t_SEMICOLON = r';'
t_ignore    = ' \t\n'

# Token Rules with Functions (NO CHANGE)
def t_HEXCOLOR(t):
    r'\#[0-9a-fA-F]{3,6}'
    return t

def t_ID_SELECTOR(t):
    r'\#[a-zA-Z_][a-zA-Z0-9_-]*'
    return t

def t_CLASS_SELECTOR(t):
    r'\.[a-zA-Z_][a-zA-Z0-9_-]*'
    return t

def t_UNITS(t):
    r'(px|em|rem|%)'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9-]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# --- THIS FUNCTION IS UPDATED ---
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.error_found = True  # <-- THIS IS THE NEW LINE
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()