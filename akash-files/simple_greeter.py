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
