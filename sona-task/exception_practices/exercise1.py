'''
Exercise 1: Handling Invalid Input
Task: Write code that asks the user for their age. 
Since input() returns a string, you must convert it to an integer. 
If the user enters text that isn't a number (like "twenty"), a ValueError will occur.
Handle this error.
'''

try:
    age_str = input("Please enter your age: ")
    age_int = int(age_str)
    print(f"You are {age_int} years old.")
# Add your except block here
except ValueError:
    print("Invalid input! Please enter a valid number for your age.")
