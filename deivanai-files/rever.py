# Your code here
def brute_force_reverse(word):
    reverse_a= ""
    for ch in range(len(word)-1,-1,-1):
        reverse_a+=word[ch]
    return reverse_a

    

# --- Test Cases ---
reversed1 = brute_force_reverse("engineer")
print(f"'engineer' reversed is '{reversed1}'")  # Expected: 'reenigne'

reversed2 = brute_force_reverse("racecar")
print(f"'racecar' reversed is '{reversed2}'") # Expected: 'racecar'