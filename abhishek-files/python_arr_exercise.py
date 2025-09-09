# 1.Check for duplicates in an array
def contains_duplicate(nums):
    # Using a set to track seen numbers
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Test cases
print(contains_duplicate([1, 2, 3, 1]))  # True
print(contains_duplicate([1, 2, 3, 4]))  # False

# 2.Find the largest word in a string
import re

def largest_word(text):
    # Extract words (alphanumeric only)
    words = re.findall(r"[a-zA-Z0-9]+", text)
    # Find the longest word
    return max(words, key=len)


# Test case
print(largest_word("fun&!! time2$3 !cat"))  # Output: time2



# 3. Two Sum Problem
def two_sum(nums, target):
    # Dictionary to store numbers and their indices
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]  # Found indices
        lookup[num] = i
    return []


# Test case
nums = [4, 6, 1, 9, 3, 5, 0, 7, 2]
target = 16
print(two_sum(nums, target))  # [3, 7]