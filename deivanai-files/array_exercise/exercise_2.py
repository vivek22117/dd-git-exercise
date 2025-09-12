# """ Question 2
# Find the largest word in a given string
# Examples
# Input: "fun&!! time2$3 !cat"
# Output: time
# """

def largest(s):
    new_sen = " "
    for letter in s:
        if letter.isalpha() or letter == " ":
            new_sen+=letter
    print(new_sen)
    
    new_word = new_sen.split()
    large = new_word[0]
    for i in new_word:
        if len(i) > len(large):
            large = i
    return large            
    
sen = "fun&!! time2$3 !cat"
print(f"The largest word of given sentence is : {largest(sen)}")












#print(lrgest)
# worl_l = sent.split()
# new_l = []
# for word in worl_l :
#     w =""
#     for letter in word:
#         if letter.isalpha():
#             w+=letter
#     new_l.append(w) 
# print(new_l)
# largest_w = new_l[0]           
# for wrd in new_l:
#     if len(wrd) > len(largest_w):
#         largest_w =wrd

# print(largest_w)


