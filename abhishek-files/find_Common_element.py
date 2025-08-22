#your code here

def find_common_elements(list1,list2):
  return set(list1) & set(list2)

#Example Usage 

list_a = [1,2,3,4,5,1,4]
list_b = [4,5,6,7,8,5]

common = find_common_elements(list_a , list_b)
print(f"List A:{list_a}")
print (f"List B:{list_b}")
print (f"Common Elements{common}")
