# your code here
def count_word_frequency(sentence):
    # Convert to lowercase to make counting case-insensitive
    words = sentence.lower().split()
    frequency = {}
    
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency

# Example Usage
my_sentence = "The quick brown fox jumps over the lazy dog"
word_counts = count_word_frequency(my_sentence)
print(f"Sentence: '{my_sentence}'")
print(f"Word Counts: {word_counts}")
