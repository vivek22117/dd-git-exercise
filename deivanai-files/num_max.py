def  find_max(number):
    
    max_num = number[0]
    for valu in number:
        if valu < max_num:
            max_num = valu
    return max_num
numbers1 = [1,41, 12, 9, 74, 15]
print(f"The max number in {numbers1} is: {find_max(numbers1)}") 

numbers2 = [-10, -5, -2, -1]
print(f"The max number in {numbers2} is: {find_max(numbers2)}")
    