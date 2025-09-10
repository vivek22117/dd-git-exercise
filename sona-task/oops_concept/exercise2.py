'''
Scenario: Imagine you are a software developer for a TV manufacturing company called "TechVision". You need to create a DigitalTv class that will serve as a blueprint for all the smart TVs your company produces.

Part 1: Basic TV Functionality
Instructions: Create a Python class named DigitalTv with the following specifications.
1. Constructor (__init__ method):
The constructor should accept brand, model, and screen_size as arguments.
It should initialize the following instance attributes:
self.brand
self.model
self.screen_size
self.is_on (should default to False)
self.channel (should default to 1)
self.volume (should default to 10)
2. Methods: Implement the following methods inside the class:
turn_on(self):
If the TV is off, this method should change self.is_on to True and print a message like "Welcome! {brand} TV is turning on.".
If the TV is already on, it should print a message like "{brand} TV is already on.".
turn_off(self):
If the TV is on, this method should change self.is_on to False and print a message like "{brand} TV is turning off.".
If the TV is already off, it should do nothing but print a message like "{brand} TV is already off.".
display_info(self):
This method should print the TV's specifications (brand, model, screen size).
It should also display the TV's current status.
If the TV is ON, it should also display the current channel and volume.
If the TV is OFF, it should only state that the status is OFF.

Part 2: 
For an extra challenge, add the following methods to your DigitalTv class:
change_channel(self, new_channel):
This method should only work if the TV is on.
If the TV is on, it should update self.channel to the new_channel value and print a confirmation.
If the TV is off, it should print a message like "Cannot change channel, the TV is off.".
adjust_volume(self, amount):
This method should also only work if the TV is on.
It should take an amount (which can be a positive or negative number) and add it to self.volume.
Constraint: The volume should never go below 0 or above 100.
If the TV is off, it should print a message like "Cannot adjust volume, the TV is off.".
'''

class DigitalTv:
    def __init__(self,brand,model,screen_size):
        self.brand=brand
        self.model=model
        self.screen_size=screen_size
        
        self.is_on=False
        self.channel=1
        self.volume=10
        
    def turn_on(self) :
        if not self.is_on:
            self.is_on=True
            print(f"Welcome! {self.brand} Tv is turning on ....")
        else:
            print(f"{self.brand} TV is already on ..")
            
    def turn_off(self):
        if self.is_on:
            self.is_on=False
            print(f"{self.brand} TV is turning off ...")
        else:
            print(f"{self.brand} TV is already off ..")
    
    def change_channel(self,new_channel):
        if self.is_on:
            self.channel=new_channel
            print(f" channel changed to {new_channel}")
        else:
            print(" Cannot change channel , the TV is OFF..")
    
    def adjust_volume(self,amount):
        if self.is_on:
            sum = self.volume + amount
            if sum >=0 and sum <= 100:
                self.volume += amount
                print(f" the updated TV volume is {self.volume}")
        else:
            print("Cannot adjust volume, the TV is off")
    
            
    
    def display_info(self):
        print(f"TV specification : \n brand : {self.brand} \n model: {self.model} \n screen_size{self.screen_size}\n TV status: {'ON ' if self.is_on else 'OFF'}")
        if self.is_on:
            print(f" TV channel : {self.channel} \n volume :{self.volume}")
        
        
samsung=DigitalTv("samasung Tv",1998,23)
samsung.turn_on()
samsung.display_info()
samsung.turn_off()
samsung.change_channel(12)
samsung.turn_on()
# samsung.adjust_volume(10)
samsung.adjust_volume(9)
samsung.adjust_volume(-15)  
           
samsung.adjust_volume(-4)