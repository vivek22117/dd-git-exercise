######################################
########## Adding two numbers ########
######################################
num1=10
num2=20
sum=num1+num2
print(sum)



###############################################
###### choice random number from list ###########
###############################################

import random 

l1=[1,2,"sonali",3.23]
b=random.choice(l1)
print(b)

############################### Number guessing game ######################
print("Welcome to the number guessing game !")

print("thinking the number between 1 to 100 ")

attempts=10

print(f"you have {attempts} attempts to guess the number ")

random_number=random.randint(1,101)



while attempts>0:
    print(f"you have {attempts} attempts ")
    guess=int(input("make a guess: "))
    
    if guess==random_number:
        print(f"you're correct the number is : {random_number}")
        break
    elif guess >random_number:
        print(f" Too high try Again !!")
    else:
        print("Too low try Again !!") 
        
    attempts -=1
