'''
Exercise 2: Safe Dictionary Access
Task: Create a function get_capital(city_dict, country) that safely retrieves a capital from a dictionary.
Use a try block to access the key (country).
Handle the KeyError if the country doesn't exist.
Use an else block to print the capital if it's found.
Use a finally block to print "City lookup complete."

'''


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
        
get_capital(capitals,"japan")
get_capital(capitals,"Japan")

