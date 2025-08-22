def find_max(numbers):
  max_no = numbers[0]
  i = max_no
  
  for i in numbers:
   if i>max_no:
     max_no = i   

  return max_no

numbers1 = [3, 41, 12, 9, 74, 15]
print(f"The max number in {numbers1} is: {find_max(numbers1)}")

numbers2 = [-10, -5, -2, -1]
print(f"The max number in {numbers2} is: {find_max(numbers2)}") 