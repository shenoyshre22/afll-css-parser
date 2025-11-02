# lexer.py

import ply.lex as lex

# List of token names
tokens = (
    'IDENTIFIER',
    'ID_SELECTOR',
    'CLASS_SELECTOR',
    'NUMBER',
    'UNITS',
    'HEXCOLOR',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'COLON',
    'SEMICOLON',
)

# --- Simple Token Rules (no conflicts) ---
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_COMMA     = r','
t_COLON     = r':'
t_SEMICOLON = r';'
t_ignore    = ' \t\n' # Ignored characters (spaces, tabs, newlines)

# --- Token Rules with Functions (Priority matters!) ---
# These are checked in order from top to bottom.

def t_HEXCOLOR(t):
    r'\#[0-9a-fA-F]{3,6}'
    # Must be defined BEFORE t_ID_SELECTOR
    return t

def t_ID_SELECTOR(t):
    r'\#[a-zA-Z_][a-zA-Z0-9_-]*'
    # Will only match if it's not a HEXCOLOR
    return t

def t_CLASS_SELECTOR(t):
    r'\.[a-zA-Z_][a-zA-Z0-9_-]*'
    return t

def t_UNITS(t):
    r'(px|em|rem|%)'
    # Must be defined BEFORE t_IDENTIFIER
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9-]*'
    # Will match p, h1, color, font-size, red, bold, etc.
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()