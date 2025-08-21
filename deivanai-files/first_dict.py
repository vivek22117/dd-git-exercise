""" Task: Create a dictionary to store information about your favorite movie. It should include the title, director, and release_year."""

# Create your movie dictionary here
favorite_movie = {
    "Title" :"Friends",
    "Director" : "Siddique",
    "release_year": 2001

    }

# Print the dictionary to see the result
print(favorite_movie)

""" Task: From the product dictionary provided, access and print the price of the item."""
product = {
    "Name" : "Moblie",
    "Price" : 45000,
    "In_Stock" : True,
    "Brand" : "Iphone"
}

# Access the price using its key
product_price = product["Price"]

print(f"The price of the product is: ${product_price}")

""" Task: You have a dictionary representing a user's profile. Add a new key country with the value 'USA'."""

user_profile = {
    "username": "Deiva",
    "email": "Deivaa123.com"
}

# Add the new key-value pair here
user_profile["country"] = "USA"
user_profile["Phone_Number"] = 788787988

print(user_profile)

""" Task: The inventory dictionary for a t-shirt is incorrect. Update the quantity from 50 to 45."""

inventory = {
    "item": "T-Shirt",
    "color": "Blue",
    "quantity": 50
}

# Update the quantity here
inventory["quantity"] = 45
inventory["color"] = "Red"

print(inventory)

"""Task: A student's record contains a temporary note that needs to be removed. Delete the temp_note key from the student_record."""

student_record = {
    "id": 201,
    "name": "John",
    "grade": "A",
    "temp_note": "Needs to submit paperwork."
}

# Delete the temp_note here
del student_record["temp_note"]

print(student_record)

""" Task: Loop through the capitals dictionary and print each country and its capital in a formatted string.
"""
capitals = {
    "USA": "Washington D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
   }
capitals["India"] = "Delhi"

# Loop through the dictionary here
for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}.")

