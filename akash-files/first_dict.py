#Create a dictionary to store information about your favorite movie. 
# It should include the title, director, and release_year.

favourite_movie= {
    "Title":"interstellar",
    "Director":"chris_nolan",
    "release_year":"2011"
    }
print(favourite_movie)


#From the product dictionary provided, access and print the price of the item.

product = {
    "name":"laptop",
    "price":1200,
    "in_stock":"True",
    "brand":"Techno"
}
product_price = product["price"]
print(f"The price of the product is: ${product_price}")

#You have a dictionary representing a user's profile. Add a new key country with the value 'USA'.

user_profile = {
    "username":"jane_doe",
    "email":"janedoe@email.com"
}

user_profile["country"]= "USA"
print(user_profile)

#The inventory dictionary for a t-shirt is incorrect. 
# Update the quantity from 50 to 45.

inventory = {
    "item":"T-shirt",
    "color":"Blue",
    "quantity":50
}
print(inventory)
inventory["quantity"]="45"
print(inventory)

 #A student's record contains a temporary note that needs to be removed. 
 # Delete the temp_note key from the student_record.

student_record = {
    "id":101,
    "name":"john snow",
    "grade":"A",
    "temp_note":"Needs to submit paperwork."
}
print(student_record)
del student_record["temp_note"]
print(student_record)

#Loop through the capitals dictionary and print each country and its capital in a formatted string.

capitals = {
    "USA":"washinto D.C",
    "France":"paris",
    "japan":"Tokyo",
    "India":"Delhi"
}

capitals["England"]="London"

for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}.")