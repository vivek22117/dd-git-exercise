'''Given an array of integers nums and an integer target, return indices/index of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.-

Input: [4, 6, 1, 9, 3, 5, 0, 7, 2], Target Sum = 16
Output: [3, 7]  # Index of “9” and “7” sums to 16
'''

def numbers(list_num,target):
    for num_1 in range(len(list_num)):
        for num_2 in range(num_1+1,len(list_num)):
            if list_num[num_1]+ list_num[num_2] == target:
                return [num_1,num_2]

list = [4, 6, 1, 9, 3, 5, 0, 7, 2]
target = int(input("enter the target number :"))
print(numbers(list,target)) 



# sum_of = list_num[2]+list_num[5]
# print(sum_of)