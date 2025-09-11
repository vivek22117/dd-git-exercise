try:
    age_str = input("Please enter your age: ")
    age_int = int(age_str)
    print(f"You are {age_int} years old.")
# Add your except block here
except ValueError:
    print("Invalid input! Please enter a valid number for your age.")

#___________________________________________________________________________________________________

""" Task: Create a function get_capital(city_dict, country) that safely retrieves a capital from a dictionary.
Use a try block to access the key (country).
Handle the KeyError if the country doesn't exist.
Use an else block to print the capital if it's found.
Use a finally block to print "City lookup complete."
"""

capitals = {
    "USA": "Washington D.C.",
    "France": "Paris",
    "Japan": "Tokyo",
    "India": "Delhi"
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
country = input("Enter the country name :")
get_capital(capitals,country)
print("-" * 25)
get_capital(capitals, "Germany")

