def find_common_element(list_a,list_b):
  # a={}
# list_a=[1,2,43]
# list_b=[2,19]
 set_a= set()
 for i in list_a:
    for val in list_b:
       if i == val:
         set_a.add(i)
 return set_a            
       
def kind_common_element(list_a,list_b):
 set_a= set()
 for i in list_a:
    if i in list_b:
      set_a.add(i)
 return set_a     



def alternate_method(a, b):
  return set([n for n in a if n in b])

            
           
#   return(a)
b=[1,2,4,6,10]
c=[2,3,4,10,11]
print(kind_common_element(b,c))   
# print(alternate_method(b, c))
