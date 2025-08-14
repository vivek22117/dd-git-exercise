# def find_max(number=list):
#   if number != list:
#     print("please provide array/list data type")
#   elif len(number) == 0:
#     print("empty list provided.")
#   else:
    
# def find_max(number):
#   max_num=number[0]
#   for i in number:
#     if i > max_num:
#       max_num = i
#       print(max_num)

# number=[3,19,2,10]
# find_max(number)

def Find_maxnumber(number_list):
  largest_value=number_list[0]
  for number in number_list:
    if number > largest_value:
      largest_value = number
  return largest_value



numbers1_list=[3,20,36,10,4,88,0,200]
print(f"The max number in {numbers1_list} is:{Find_maxnumber(numbers1_list)}")
# Find_maxnumber()      
  
   
# def max_number(number):
#   largest_value=number[0]
#   i
#   while i > largest_value:
#     pass