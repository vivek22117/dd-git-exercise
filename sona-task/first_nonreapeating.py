'''
Question 5
Find the index of the first non-repeating character in a string.
 Return the index (0-based). If none exists, return -1.
Examples
 Input: "leetcode" → Output: 0 (’l’ is unique)
 Input: "aabbccdde" → Output: 8 (’e’ is first unique)
 Input: "aabb" → Output: -1
'''

new="leetcode"
empty_list=set()
for i in new:
    if i not in empty_list:
        print(i)
        
        




