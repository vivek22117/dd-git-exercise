# def duplicates(list1):
#    list2=set()
#    for  i in list1:
#       if i in list2:
#          return True
#       list2.add(i)
#    return False   
            
# array1=[1,2,3,1]
# print(duplicates(array1))


# arr_int=[1,2,3,4,5,2]
# b=list(set(arr_int))
# print(arr_int!=b)
###
# def check_duplicate(arr_int):
#   set_int=set(arr_int)
#   return arr_int!=set_int
# print(check_duplicate(arr_int=[1,2,3]))



###largest word in a given string
sentence="fun&!! time2$3 !cat"
new_sentence=''
for word in sentence:
   if word.isalpha() or word== " ":
      new_sentence+=word

print(new_sentence)      
new_list=new_sentence.split()
character=new_list[0]
for i in new_list:
   if len(i) > len(character):
      character=i
print(character)      
   




