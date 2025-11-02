# main.py

from lexer import lexer
from parser import parser, PARSE_ERROR_FLAG  # Import the flag
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
    
    result = parser.parse(input_data, lexer=lexer)
    
    print("-----------------------")
    
    # Check the flag INSTEAD of the 'result'
    if not PARSE_ERROR_FLAG:
        print(" Syntax: Accepted YAY")
    else:
        print(" Syntax: Rejected (See error messages above)")