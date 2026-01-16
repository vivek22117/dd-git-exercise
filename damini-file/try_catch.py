

# file = open("code.json")
# # try:
# #   file = open("file.txt")
# # except FileNotFoundError as e:
# #   print(e)
  


# # sum = 1 + 2

# # print(sum)

# '''C:\developement\project\dd-git-exercise\damini-file\file.txt'''

# "C:\developement\project\dd-git-exercise\damini-file\code"

###Try -Except block
# try:
#   numerator=20
#   denominator=0
#   result=numerator/denominator
#   print(result)

# except ZeroDivisionError:
#        print("Error:You can't divide by zero!")
# print("The program Continued without crashing")   


###Handling Invalid Input
# try:
#      age_str=input("Please Enter your age: ")
#      age_int = int(age_str)
#      print(f"You are {age_int} years old.")
# except ValueError:
#      print("Invalid input! Please enter a valid number for your age.")     

# ###Safe Dictionary Access
# capitals = {
#      "USA" : "Washington D.C.",
#      "France" : "Paris",
#      "Japan" : "Tokyo"
# }     

# def get_capital(city_dict, country):
   
#   try:
#       capitals = city_dict[country]
#   except KeyError:
#       print(f"Error: The country '{country}'was not found in our records")
#   else:
#     print(f"The capital of {country} is {capitals}") 
#   finally:
#       print("City lookup complete") 

#test case 
# get_capital(capitals,"France")
# print("-"* 20)
# get_capital(capitals,"USA")



##Handling Multiple , Specific Exceptions
def process_item(data,index):
    try:
        item = data[index]          # fetch element at index
        result = item + 5           # try to add 5
        print(f"The result is:{result}")
    except IndexError:
        print(f"Error:Index {index} is out of bounds for the list.")
    except TypeError:
        print(f"Error : The item at index {index} is not a number and can't be added.")

my_list=[10,20,"hello",40]

process_item(my_list, 1)
process_item(my_list, 10)
process_item(my_list, 3)


##Inspecting the Exception Object with as
try:
    with open("non_existent_file.txt","r") as file:
        content =file.read()
except FileNotFoundError as e :
    print("Failed to open file.")
    print(f"Reason: {e}")
except Exception as e:
    print(f"An unexpected error occured: {e}")           