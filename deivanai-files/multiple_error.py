def process_item(data, index):
    try:
        item = data[index]
        result = item + 5
        print(f"The result is: {result}")
    except IndexError:
        print(f"Error: Index {index} is out of bounds for the list.")
    except TypeError:
        print(f"Error: The item at index {index} is not a number and can't be added.")
     

my_list = [0,10, "hello", 40,"a+2"]

process_item(my_list, 1)  # Success
process_item(my_list, 0) # Triggers IndexError
process_item(my_list, 5)  # Triggers TypeError

#________________________________________________________________________________________________________

try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print("Failed to open file.")
    print(f"Reason: {e}") # 'e' is the exception object, which contains the message
except Exception as e:
    print(f"An unexpected error occurred: {e}")

