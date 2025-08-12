
def brute_force_reverse(s):
  string = "" 
  for i in range(len(s)-1, -1, -1):
    string += s[i]
  return string
reversed1 = brute_force_reverse("engineer")
print(f"'engineer' reversed is '{reversed1}'")  

reversed2 = brute_force_reverse("racecar")
print(f"'racecar' reversed is '{reversed2}'") 