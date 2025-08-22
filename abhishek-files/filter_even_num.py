def filter_even_numbers(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

# Example Usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter_even_numbers(my_list)
print(f"Original List: {my_list}")
print(f"Even Numbers: {evens}")
