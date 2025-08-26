# Exercise 1: Handling Invalid Input

try:
    age_str = input("Please enter your age: hellow")
    age_int = int(age_str)   # Try converting input to integer
    print(f"You are {age_int} years old.")
except ValueError:
    print("Invalid input! Please enter a valid number for your age.")

# Exercise 2: Safe Dictionary Access

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

# Handling Multiple, Specific Exceptions


