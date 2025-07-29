"""This code is used to check weather the given numbers is odd or even"""

# num = int(input("Give any number : "))
# if num%2==0:
#     print(f"{num} is an even numer")
# else:
#     print(f"{num} is an odd number")


    #####################################
    ###### FIZZ BUZZ GAME ###################
    #######################################

for num in range(1,101):                 #Looping from 1 to 100
    if num%3==0 and num%5==0:
        print("Fizz-Buzz")               #Printing fizzBuzz when the number is divisible by both
    elif num%3==0:
        print("Fizz")                    #Printing Fizz when the number divisible by 3 
    elif num%5==0:
        print("Buzz")                    #Printing Buzz when the number divisible by 5
    else: 
        print(num)                                
           

 

