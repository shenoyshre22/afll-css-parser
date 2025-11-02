# lexer.py
# This file is based on the structure in 7.1 lexer.py of your tutorial [cite: 323]

import ply.lex as lex

# List of token names. This is always required [cite: 98, 325]
tokens = (
    'IDENTIFIER',     # p, h1, color, font-size, red, bold
    'ID_SELECTOR',    # #header
    'CLASS_SELECTOR', # .button
    'NUMBER',         # 14, 1
    'UNITS',          # px, %, em
    'HEXCOLOR',       # #FFF, #ff0000
    'LBRACE',         # {
    'RBRACE',         # }
    'COMMA',          # ,
    'COLON',          # :
    'SEMICOLON',      # ;
)

# Regular expression rules for simple tokens
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_COMMA     = r','
t_COLON     = r':'
t_SEMICOLON = r';'
t_HEXCOLOR  = r'\#[0-9a-fA-F]{3,6}'
t_UNITS     = r'(px|em|rem|%)'

# A string containing ignored characters (spaces, tabs, newlines) [cite: 334]
t_ignore = ' \t\n'

# --- Token Rules with Functions ---
# We use functions for tokens that need extra logic or to be prioritized

def t_ID_SELECTOR(t):
    r'\#[a-zA-Z_][a-zA-Z0-9_-]*'
    # This regex matches a '#' followed by a valid CSS ID name
    return t

def t_CLASS_SELECTOR(t):
    r'\.[a-zA-Z_][a-zA-Z0-9_-]*'
    # This regex matches a '.' followed by a valid CSS class name
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9-]*'
    # This matches element names (p, h1) and property names (color, font-size)
    # and some values (red, bold)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Convert the string '14' to the number 14
    return t

# Error handling rule [cite: 102, 336]
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer [cite: 106, 343]
lexer = lex.lex()