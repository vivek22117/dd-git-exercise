num = int(input("give any number : "))
print(num)
if num % 2 == 0:
  print("number is even")
else:
  print("number is odd")
even_list =[]
odd_list =[]
for i in range(1,11):
  if i % 2 != 0:
    print(i)
    odd_list.append(i)
  else:
    even_list.append(i) 

##############################################################################
print("Hello World")
