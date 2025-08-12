# Your code here
def brute_force_reverse(string):
  """for returning reversed string"""
  reversed_string=""
  ln=len(string)
  for i in range(ln-1,-1,-1):
    reversed_string+=string[i]
 
  return reversed_string

# --- Test Cases ---
reversed1 = brute_force_reverse("engineer")
print(f"'engineer' reversed is '{reversed1}'")  # Expected: 'reenigne'

reversed2 = brute_force_reverse("racecar")
print(f"'racecar' reversed is '{reversed2}'") # Expected: 'racecar'