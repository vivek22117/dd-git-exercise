'''
Question 3
Given an array of integers nums and an integer target, return indices/index of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Input: [4, 6, 1, 9, 3, 5, 0, 7, 2], Target Sum = 16
Output: [3, 7]  # Index of “9” and “7” sums to 16

'''
# Input= [4, 6, 1, 9, 3, 5, 0, 7, 2]
# target=16
# # len_input=len(Input)
# # print(len_input)
# for start in range(len(Input)):
#     for end in range( len(Input)-1):
#         # print(Input[start], " + " ,Input[end+1], "=", Input[start]+Input[end+1])
#         if Input[start]+Input[end+1]==target:
#             print(f"{Input[start]} + {Input[end+1]}")
#             print(f"{Input.index(Input[start])} , {Input.index(Input[end])}")

###########################################################################################
            
def target_sum(input,target):
    # target=16
    for start in range(len(input)-1):
        for end in range(len(input)-1):
            if input[start] + input[end+1]==target:
                print(f" {input[start] }  + { input[end+1] }")
                print(f" {input.index(input[start])} , {input.index(input[end+1])}")
                return
target_sum(input=[4, 6, 1, 9, 3, 5, 0, 7, 2] ,target=16)
    
###########################################################################################

def target_addition(input,target):
    # target=16
    for start in range(len(input)-1):
        for end in range(len(input)):
            if input[start] + input[end]==target:
                print(f" {input[start] }  + { input[end] }")
                print(f" {input.index(input[start])} , {input.index(input[end])}")
                return
target_sum(input=[4, 6, 1, 9, 3, 5, 0, 7, 2] ,target=15)
    