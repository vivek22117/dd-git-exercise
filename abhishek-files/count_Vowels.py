 # Your code here
def count_vowels(text):
    vowels = "aeiou"  # All vowels
    text = text.lower()  # Make it case-insensitive
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
    return count

# --- Test Cases ---
sentence1 = "Hello World"
print(f"Vowel count in '{sentence1}': {count_vowels(sentence1)}") # Expected: 3

sentence2 = "Programming is fun"
print(f"Vowel count in '{sentence2}': {count_vowels(sentence2)}") # Expected: 5


