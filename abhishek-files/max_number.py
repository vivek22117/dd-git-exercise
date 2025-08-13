# Your code here
def find_max(numbers):
    # Assume the first number is the largest initially
    max_num = numbers[0]
    
    # Loop through the list
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


# --- Test Cases ---
numbers1 = [3, 41, 12, 9, 74, 15]
print(f"The max number in {numbers1} is: {find_max(numbers1)}")  # Expected: 74

numbers2 = [-10, -5, -2, -1]
print(f"The max number in {numbers2} is: {find_max(numbers2)}")  # Expected: -1
