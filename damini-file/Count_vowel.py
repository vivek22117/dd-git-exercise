#code here
def count_vowels(input_string):
  vowels="aeiou"
  count=0
  input_string = input_string.lower()
  #print(input_string)
  for i in input_string:
    if i in vowels:
      count+=1
  return count

# count_vowels("DJHFKSJDNVMDNLSJDPOMDKLFOERIWKENWEQA")
input_string= "Hello World"
print(f"Vowel count in '{input_string}':  {count_vowels(input_string)}")
 


      
      

  


  

