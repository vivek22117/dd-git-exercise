# Your code here
def count_word_frequency(sentence):
    word_freq = dict()
    list_of_words = my_sentence.split()
    print(list_of_words)
    for word in list_of_words:
        word = word.lower()
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1
    return word_freq        





    



# Example Usage
my_sentence = "The quick brown fox fox jumps over over the lazy dog"
word_counts = count_word_frequency(my_sentence)
print(f"Sentence: '{my_sentence}'")
print(f"Word Counts: {word_counts}")
# Expected Output: Word Counts: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, '
