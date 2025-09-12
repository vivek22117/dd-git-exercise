#Given an array of integers, find if the array contains any duplicates.
#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

""" Example 1:
Input: [1,2,3,1]
Output: true
"""
def is_duplicate(number):
    a = set(number)
    return len(a) !=len(number)

input = [1,3,5]
print(is_duplicate(input))
# print(input)
# print(set(input))


