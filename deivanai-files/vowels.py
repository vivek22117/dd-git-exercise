def count_vowels(sentence):
    vowels = "aeiou"
    count = 0
    sentence = sentence.lower()
    for chr in sentence:
        if chr in vowels:
            count +=1
    return count        

text = "HEllo World"

print(f"Vowel count in '{text.lower()}': {count_vowels(text)}")
