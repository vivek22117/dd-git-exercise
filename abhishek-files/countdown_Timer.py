# Your code here

def countdown(start_num):
    # Ensure input is positive
    if start_num <= 0:
        print("Please enter a positive integer.")
        return
    
    while start_num > 0:
        print(start_num)
        start_num -= 1  # Decrease by 1 each loop
    print("Blast off!")

# --- Test Case ---
print("Starting 5-second countdown:")
countdown(5)

# Expected Output:
# 5
# 4
# 3
# 2
# 1
# Blast off!
