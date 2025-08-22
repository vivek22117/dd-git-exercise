def count_words_frequency(sentence):
  create_dic={}
  sentence=sentence.lower()
  sentence=sentence.split()
  for word in sentence:
    if word in create_dic:
      create_dic[word] += 1
    else:
      create_dic[word] = 1
  return create_dic

sentence="The quick brown fox jumps over the lazy dog" 
word_counts = count_words_frequency(sentence)
print(f"Sentence: '{sentence}'")
print(f"Word Counts: {word_counts}")   
