'''
Check if two strings are anagrams (letters only, case-insensitive).
 Ignore spaces, punctuation, and digits.
Create a function : is_anagram(w1, w2)
Examples
 Input: "Dormitory", "Dirty room!!"     #ignoring space and punctuations
 Output: true							#only letters
Input: "Listen", "Silent?"
 Output: true
Input: "Hello", "Olelh!!!1"	     #ignoring punctuation and number
 Output: true
Input: "Apple", "Pabble"
 Output: false
'''



   
d1={}
d2={}

def is_anagram(w1, w2):
    for ch in w1:
        if ch.isalpha():
            ch = ch.lower()
            if ch in d1:
                d1[ch] += 1
            else:
                d1[ch] = 1 
    for ch in w2:
        if ch.isalpha():
            ch=ch.lower()
            if ch in d2:
                d2[ch] += 1
            else:
                d2[ch] =1
    
    return d1 == d2

print(is_anagram("sonali" ,"osnali"))
print(is_anagram("LiSten", "silent?"))
print(is_anagram("Hello", "Olelh!!!1"	))