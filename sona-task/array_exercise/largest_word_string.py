'''
Question 2
Find the largest word in a given string
Examples
Input: "fun&!! time2$3 !cat"
Output: time
'''

# mystring= "fun&!! time2$3 !cat"
# mystring=mystring.split()
# print(mystring)
# new=[]
# for let in mystring:
#     empty_letter=" "
#     for j in let:
#         if j.isalpha():
#             empty_letter+=j
#     new.append(empty_letter)
# print(new)


     
# max_str=new[0]
# for i in new:
#     if i>max_str:
#         max_str=i
# print(max_str)


def large_word(str):
    large_word_list=[]
    new_str=str.split()
    print(new_str)
    for let in new_str:
        letter=" "
        for i in let:
            if i.isalpha():
                letter+=i
        large_word_list.append(letter)
        
    
    a=""
    for i in large_word_list:
        if len(i)>len(a):
            a=i
    return a
        

print(large_word(str="fun&!! time2$3 ")) 
        
    # max_word=large_word_list[0]
    # for i in large_word_list:
    #     if i>max_word:
    #         max_word=i
            
            
    # return max_word
    
    # for i in large_word_list:
    #     if len(i)>len(large_word_list):
    #      large_word_list=i
    # return large_word_list
    
    
    

        



### way 2

mystring="fun&!! time2$3 !cat"
new_str= ""
for i in mystring:
    if i.isalpha() or i==" ":
        new_str+=i
    
print(new_str )
nlist = new_str.split()
large_char = nlist[0]
for i in nlist:
    if len(i) > len(large_char):
        large_char=i
print(large_char)


def find_large_word(input):
    empty_str=""
    for i in input:
        if i.isalpha() or i== " ":
            empty_str+=i
    print(empty_str)
    new_list=empty_str.split()
    largest_word=empty_str[0]
    for word in new_list:
        if len(word)>len(largest_word):
            largest_word=word
    print(largest_word)

find_large_word(input="@#$sonaliiii #$devaa #$!damini ")