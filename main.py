# main.py
# This file is based on the structure in 7.3 main.py of your tutorial [cite: 360]

from lexer import lexer   # [cite: 361]
from parser import parser # [cite: 362]
import sys

print("CSS Syntax Validator")
print("Enter your CSS code.")
print("On a new line, press Ctrl+D (Linux/Mac) or Ctrl+Z+Enter (Windows) when done.")
print("-----------------------------------------------------------------------------")

# Read all lines of input from the user
try:
    input_data = ""
    while True:
        line = input()
        input_data += line + '\n'
except EOFError:
    pass # User has finished entering input

if not input_data.strip():
    print("No input provided. Exiting.")
else:
    print("\n--- Parsing Input ---")
    
    # Run the parser on the entire input string
    # The 'lexer' is automatically used by the parser
    result = parser.parse(input_data) # [cite: 366]
    
    # The p_error function (in parser.py) will print any syntax errors.
    # If no errors were found, 'result' will be None (or the value from the top rule)
    # and we can consider it "Accepted".
    
    print("-----------------------")
    # This check is based on your tutorial's main file [cite: 367]
    if result is not None:
        print(" Syntax: Accepted YAY")
    else:
        # Note: p_error will have already printed the specific error.
        print(" Syntax: Rejected (See error messages above)")