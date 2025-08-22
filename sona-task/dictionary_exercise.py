# Dictionary examples

student_data={
    "id": 1,
    "name": "sonali",
    "age":21,
     "major":"computer science"
      
} 
print(student_data)
print(type(student_data))

###Example1###

favorite_movie ={
    "title" : "Titanic" ,
    "year": 1997,
    "genre": "Drama",
    "director": "James Cameron",
    "rating": 7.8
}

print(favorite_movie)


# Accessing values

product ={
    "name": "Laptop",
    "price" : 1200,
    "in_stock":True,
    "brand" :"TechCo"
    
}

#Access the price using its key

product_price =product["price"]
print(f"The price of the product is :${product_price}") 


#Adding a new key-value pair

user_profile={
    "username":"jahn_doe",
    "email":"jane@example.com"

}

user_profile["country"]="USA"

print(user_profile)


#Modifying an existing value

inventory={
    "item": "T-shirt",
    "color":"Blue",
    "Quantity":50
}

inventory["Quantity"]=45

print(inventory)

#Deleting a key value pair
student_record = {
    "id": 101,
    "name": "John Smith",
    "grade": "A",
    "temp_note": "Needs to submit paperwork."
}
print(student_record)
# Delete the temp_note here
del student_record["temp_note"]
# The 'del' keyword is used to remove a key-value pair from a dictionary.
del student_record["temp_note"]


print(student_record)
student_record.pop("name")
print(student_record)

#Iterating through a dict

capitals = {
    "USA": "Washington D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
}

# Loop through the dictionary here
for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}.")

# The .items() method returns key-value pairs, which you can unpack into two variables in your loop.