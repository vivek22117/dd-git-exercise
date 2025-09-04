'''
Scenario: You're trying to open a file that doesn't exist. 
You want to show the user the exact error message from the operating system.
'''

try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print("Failed to open file.")
    print(f"Reason: {e}") # 'e' is the exception object, which contains the message
except Exception as e:
    print(f"An unexpected error occurred: {e}")
