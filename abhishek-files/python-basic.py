
# elif statement: (short for "else if") Allows for checking multiple conditions sequentially. If the if condition is False, it checks the elif condition, and so on.

score = 65

if score >= 90 :
        print("Grade A")
    
elif score >= 70:
        print("Grade B")
    
else:
        print("Grade C")

# 2. Looping Statements:
# for loop: Iterates over a sequence (like a list, tuple, string, or range) or any other iterable object, executing a block of code for each element.

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
 
        print(fruit)

# while loop: Repeatedly executes a block of code as long as a specified condition remains True.

count = 0
while count < 5:
        print(count)
        count += 1


#  3. Control Flow Altering Statements:
# break statement: Terminates the current loop entirely and transfers control to the statement immediately following the loop.


for i in range(10):
  if i == 5:
   break
print(i)
       