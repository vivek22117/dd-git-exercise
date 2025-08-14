
# Your code here
def filter_even_numbers(my_list):
    even = []
    for n in my_list:
        if n % 2 == 0:
            even.append(n)
    return even            

            #Using List comperhension     
def alternate_method(anylist):
    return [n for n in anylist if n % 2 == 0]
    



# Example Usage
my_list = [1, 2, 7, 9,15,22, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter_even_numbers(my_list)
print(f"Original List: {my_list}")
print(f"Even Numbers: {evens}")
# Expected Output: Even Numbers: [2, 4, 6, 8, 10]

#Alternate method 
my_list1 = [44,7,8,9,10,2,1,54,66,9]
res_evens_1 = alternate_method(my_list1)
print(f"Original list :"{my_list1})
print(f"Even Numbers: {res_evens_1}")