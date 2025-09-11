# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
# Example 1:
# Input: [1,2,3,1]
# Output: true

def duplicates(array):
 a = set(array)
 return len(a)!=len(array)
  
input = [1,2,3,1]
print(duplicates(input))

# Find the largest word in a given string
# Examples
# Input: "fun&!! time2$3 !cat"
# Output: time


def largest_word(string):
    new_str = string.split()
    str = []
    #print(new_str)
    for ch in new_str:
     c= ""
     for i in ch:
       if i.isalpha():
        c+=i
     str.append(c)
    #print(str)
    
    largest = ""
    for i in str:
     if len(i)>len(largest):
        largest=i
    return largest

input = "fun&!! time2$3 !cat"
print(f"The largest word is {largest_word(input)} ")


# Given an array of integers nums and an integer target, return indices/index of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Input: [4, 6, 1, 9, 3, 5, 0, 7, 2], Target Sum = 16
# Output: [3, 7]  # Index of “9” and “7” sums to 16


#array= [4, 6, 1, 9, 3, 5, 0, 7, 2]
def return_pair_of_index(array, target_sum):
 for i in range(len(array)):
      for j in range(i+1, len(array)):
        if array[i] + array[j] == target_sum:
          print(f"{array[i]} + {array[j]} = {target_sum}")
          #print(f"{array.index(array[i])} , {array.index(array[j+1])}")
          return([i, j])

Input = [4, 6, 1, 9, 3, 5, 0, 7, 2]
target_sum = 16
 
print(return_pair_of_index(Input, target_sum))