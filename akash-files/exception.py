#Task: Write code that asks the user for their age. Since input() returns a string, 
# you must convert it to an integer. 
# If the user enters text that isn't a number (like "twenty"), a ValueError will occur. 
# Handle this error.


try:
    age_str = input("Please enter your age: ")
    age_int = int(age_str)
    print(f"You are {age_int} years old.")
# Add your except block here
except ValueError:
    print("Invalid input! Please enter a valid number for your age.")


#Task: Create a function get_capital(city_dict, country) that safely retrieves a capital from a dictionary.
#1.Use a try block to access the key (country).
#2.Handle the KeyError if the country doesn't exist.
#3.Use an else block to print the capital if it's found.
#4.Use a finally block to print "City lookup complete."

capitals = {
    "USA": "Washington D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
}

def get_capital(city_dict, country):
    # Your code here
    try:
        capital = city_dict[country]
    except KeyError:
        print(f"Error: The country '{country}' was not found in our records.")
    else:
        print(f"The capital of {country} is {capital}.")
    finally:
        print("City lookup complete.")


# Test cases
get_capital(capitals, "France")
print("-" * 20)
get_capital(capitals, "Germany")


#Scenario: Imagine a function that processes a list of numbers. An error could occur 
# if the index is wrong (IndexError) or if we try to add a number to a string (TypeError).
def process_item(data, index):
    try:
        item = data[index]
        result = item + 5
        print(f"The result is: {result}")
    except IndexError:
        print(f"Error: Index {index} is out of bounds for the list.")
    except TypeError:
        print(f"Error: The item at index {index} is not a number and can't be added.")

my_list = [10, 20, "hello", 40]

process_item(my_list, 1)  # Success
process_item(my_list, 10) # Triggers IndexError
process_item(my_list, 2)  # Triggers TypeError


#You're trying to open a file that doesn't exist. 
# You want to show the user the exact error message from the operating system.

try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print("Failed to open file.")
    print(f"Reason: {e}") # 'e' is the exception object, which contains the message
except Exception as e:
    print(f"An unexpected error occurred: {e}")


