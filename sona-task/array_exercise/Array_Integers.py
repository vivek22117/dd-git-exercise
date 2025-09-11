'''
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
Example 1:
Input: [1,2,3,1]
Output: true 
'''

# a=[1,2,3,1]
# b=list(set(a))
# print(a!=b)

# def find_dublicate(a):
#     b=list(set(a))
#     return a!=b
# print(find_dublicate(a=[1,2,3]))    


# #### way 2

# a=[1,2,3]
# b=set(a)
# print(len(a)!=len(b))

# def check_duplicates(input):
#     set_arr=set(input)
#     return len(set_arr )!= len(input)

# print(check_duplicates(input=[1,2,3,4,5,1,2]))

### way 3

a="soonali"
for i in range(len(a)-1):
    print(a[i], a[i+1])
    print(a[i]==a[i+1])
    
    

def check_duplicates(a):
    a.sort()
    for i in range(len(a)):
        if a[i]==a[i+1]:
            return True
        else:
            return False
            

print(check_duplicates(a=[1,2,3,4]))


### way 4

def check_duplicate(input):
    set_arr=set()
    for i in input:
        if i in set_arr:
            return True
        set_arr.add(i)
        
    return False

print(check_duplicate(input=[1,2,34,2]))

    
    
