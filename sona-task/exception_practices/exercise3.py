# Handling Multiple, Specific Exceptions

def process_item(data, index):
    try:
        item = data[index]
        result = item + 5
        print(f"The result is: {result}")
    except IndexError:
        print(f"Error: Index {index} is out of bounds for the list.")
    except TypeError:
        print(f"Error: The item at index {index} is not a number and can't be added.")

my_list = [10, 20, "hello", 40]

process_item(my_list, 1)  # Success
process_item(my_list, 10) # Triggers IndexError
process_item(my_list, 2)  # Triggers TypeError
