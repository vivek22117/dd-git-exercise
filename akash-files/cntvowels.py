def count_vowels(string):
    vowels = "aeiou"
    v_count = 0
    string = string.lower()
    print (string)
    for i in string:
        if i in vowels:
         v_count += 1
    return v_count
sentence1 = "Hello World"
print(f"Vowel count in '{sentence1}': {count_vowels(sentence1)}")  

sentence2 = "Programming is fun"
print(f"Vowel count in '{sentence2}': {count_vowels(sentence2)}")

