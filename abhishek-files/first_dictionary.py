# 1. Create Your First Dictionary
# Create your movie dictionary here
#Task: Create a dictionary to store information about your favorite movie. It should include the title, director, and release_year.

favorite_movie = {
"title" : "Avtar",
"Director" : " James Cameron",
"realesed_year": "2009",
"budet" : "23.7 cr" ,
"collection" : "8,957 cr" ,
 "is_Hit": True 
}
# Print the dictionary to see the result
print(favorite_movie)

# 2. Accessing Values
# Task: From the product dictionary provided, access and print the price of the item.

product = {
  "name" : "Laptop" ,
  "Brand" : "HP" ,
  "price" : 50000,
  "in_Stock": True
}

# Access the price using its key
product_price = product["price"]

print (f"The price of the product is : $ {product_price}")

# 3. Adding a New Key-Value Pair
# Task: You have a dictionary representing a user's profile. Add a new key country with the value 'USA'.

user_profile = {
"username":"abhishek",
"email" : "abhishekkadale779@gmail.com",
"id": 188 

}

user_profile ["country"] = "India"

print (user_profile)

# 4. Modifying an Existing Value
# Task: The inventory dictionary for a t-shirt is incorrect. Update the quantity from 50 to 45.

inventery = {
  "item" : "t-shirt",
  "color" : "black",
  "quantity" : 50,
}

inventery ["quantity"] = 45 

print(inventery)

# Deleting a Key-Value Pair
# Task: A student's record contains a temporary note that needs to be removed. Delete the temp_note key from the student_record.

student_record = {
  "id": 101,
  "name": "john doe",
  "grade": "A",
  "temp_note":"Needs to submit paperwork"
}
# Delete the temp_note here
del student_record ["temp_note"]

print(student_record)

# 6. Iterating Through a Dictionary
# Task: Loop through the capitals dictionary and print each country and its capital in a formatted string.

capitals = {
  "INDIA":"Delhi",
  "USA":"Washington DC",
  "FRANCE":"Paris",
  "JAPAN":"Tokiyo"
}
# Loop through the dictionary here
for country, capital in capitals .items():

  print(f"The capital of {country} is {capital}.")