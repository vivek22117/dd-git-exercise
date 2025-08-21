# create dictionary
favorite_movie={
 " title" : "Bajarangi Bhaijaan",
 "Director":"Kabir Khan",
 " release_year":2016
}

#print dictionary 
print(favorite_movie)

##Accessing Values
product={
  "name":"Laptop",
  "price":20000,
  "in_stock":True,
  "brand":"HP"
}

product_price=product["price"]
print(f"The price of the product is: ${product_price}")

###Adding New key-value pair
user_profile={
  "username":"John",
  "email":"john@example.com"
  }

#Add the new key-value pair here
user_profile["city"]="Kerala"

print(user_profile)


####Modifying an existing Value
inventory={
  "item":"T-Shirt",
  "color":"Yello",
  "quantity":60
}
inventory["quantity"]=45
print(inventory)

## another example 
salary={
  "employee_name":"Julie",
  "employee_salry":12000,
   "company":"XYZ"

}

salary["employee_salry"]=20000
print(f"The Employee salary is: ${salary}")

###Deleting a key-value pair
Student_record={
  "id":100,
  "name":"John Smith",
  "grade":"B",
  "temp_note":"Needs to submit paperwork."
}
del Student_record["grade"]
print(Student_record)


###Iterating Through a Dictionary
capitals={
  "USA":"Washington D.C",
  "France":"Paris",
  "Japan":"Tokyo"
}

for country, capital in capitals.items():
  print(f"The capital of {country} is {capital}.")

information={
  "name":"Damini",
  "age":25,
  "country":"India"
}
for person,info in information.items():
  print(f"The employee {person} is: {info}") 
   