#commmand line argruments are values passed to a script when it is run from the command line.
# They allow you to customize the behavior of the script without modifying the code itself.
# In Python, you can access command line arguments using the sys module, specifically the sys.argv list.

import sys

name=sys.argv[1]  # The first argument is the script name, so we take the second one
age=sys.argv[2]  # The second argument is the age
print(f"Hello {name}, you are {age} years old!")
# To run this script from the command line, you would use a command like:
# python command_line_arg.py John 25