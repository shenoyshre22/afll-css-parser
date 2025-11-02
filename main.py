# main.py

from lexer import lexer
from parser import parser  # <-- REMOVE 'PARSE_ERROR_FLAG'
import sys

print("CSS Syntax Validator")
print("Enter your CSS code.")
print("On a new line, press Ctrl+D (Linux/Mac) or Ctrl+Z+Enter (Windows) when done.")
print("-----------------------------------------------------------------------------")

try:
    input_data = ""
    while True:
        line = input()
        input_data += line + '\n'
except EOFError:
    pass

if not input_data.strip():
    print("No input provided. Exiting.")
else:
    print("\n--- Parsing Input ---")
    
    # --- ADD THIS LINE ---
    # Reset the error flag on the lexer before each parse
    lexer.error_found = False 
    
    result = parser.parse(input_data, lexer=lexer)
    
    print("-----------------------")
    
    # --- UPDATE THIS CHECK ---
    # Check the flag on the lexer object
    if not lexer.error_found:
        print(" Syntax: Accepted YAY")
    else:
        print(" Syntax: Rejected (See error messages above)")