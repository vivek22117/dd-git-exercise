# What is sys in Python?

# sys is a built-in module in Python.

# It gives you access to system-specific parameters and functions.

# In other words, it helps Python interact with the interpreter and the operating system.

# You need to import it before use:

# import sys

# 🔹 Common Uses of sys

# Here are the most important things you’ll use sys for:

# 1. Command Line Arguments

# If you run a Python script from the command line, you can pass arguments.

# import sys
# print("File name:", sys.argv[0])   # First argument → script name
# print("Arguments:", sys.argv[1:])  # Rest → user arguments


# 👉 Example:

# python script.py hello world


# Output:

# File name: script.py
# Arguments: ['hello', 'world']

# 2. Exit the Program
# import sys
# print("Exiting now...")
# sys.exit()   # Immediately stops the program

# 3. Python Version
# import sys
# print(sys.version)

# 4. Maximum Integer Value
# import sys
# print(sys.maxsize)  # Largest integer Python can handle

# 5. Standard Input, Output, Error

# These let you read/write directly to console streams.

# import sys

# sys.stdout.write("Hello via stdout\n")  # Normal output
# sys.stderr.write("This is an error message\n")  # Error output

# # Taking input
# data = sys.stdin.readline()
# print("You entered:", data)

# 6. Check Module Search Path

# Python looks for modules in these directories when you import something.

# import sys
# print(sys.path)

# 7. Platform Information
# import sys
# print(sys.platform)  # e.g. 'win32', 'linux', 'darwin' (Mac)




#!/usr/bin/env python3
import sys

def greet_user():
    if len(sys.argv) > 1:
        # sys.argv[0] is the script name, so the first argument is at index 1
        name = sys.argv[1]
        print(f"Hello, {name}! Welcome to the command-line.")
    else:
        print("Hello! Please provide a name as an argument to get a personalized greeting.")
        print("Example: ./simple_greeter.py World")

if __name__ == "__main__":
   greet_user()