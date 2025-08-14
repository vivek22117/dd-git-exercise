def filter_even_numbers(my_list):
  even_list=[] 
  for val in my_list:
   if val % 2 == 0:
     even_list.append(val) 
  return even_list
   
my_num=[2,4,3,6,10]   
print(filter_even_numbers(my_num))      
  
def alternate_method(my_list1):
  return [val for val in my_list1 if val % 2 == 0]

my_num1=[10,29,34,4,8,86]
print(alternate_method(my_num1))

