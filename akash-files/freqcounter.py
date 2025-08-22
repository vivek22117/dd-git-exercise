def word_frequency_counter(sentence):
    sentence = sentence.lower()
    sentence = sentence.split() 
    counter={}
    for i in sentence:
        if i in counter:
          counter[i] += 1
        else:
          counter[i] = 1
    return counter

my_sentence = "The quick brown fox jumps over the lazy dog"
word_counts = word_frequency_counter(my_sentence)
print(f"Sentence: '{my_sentence}'")
print(f"Word Counts: {word_counts}")


#s = "the quick brown for jumps over the lazy dog" 
# s = s.split()
# count = {}
# print(s)
# for i in s:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1
# print(count)