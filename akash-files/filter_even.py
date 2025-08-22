def filter_even_numbers(any_list):
    #list=[x for x in my_list if x%2==0]
    res_list = []
    for num in any_list:
       if num % 2 ==0:
            res_list.append(num)
    return res_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter_even_numbers(my_list)
print(f"Original List: {my_list}")
print(f"Even Numbers: {evens}")
    
