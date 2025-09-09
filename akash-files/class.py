'''
class SuperHero:
    def __init__(self, name: str, power: str, health: int, speed: int):
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed

iron_man = SuperHero("Iron Man", "repulsor beams", 100, 80)
spider_man = SuperHero("Spider Man", "web slinging", 90, 95)

print(iron_man.power)
print(spider_man.health)

'''


class SmartDevice:
    # Class attributes: Shared across all instances of the class
    total_devices = 0
    active_devices = 0

    def __init__(self, name):
        self.name = name
        self.is_on = False

        SmartDevice.total_devices += 1

    def turn_on(self):
        
        if not self.is_on:
            self.is_on = True
            SmartDevice.active_devices += 1
            print(f"{self.name} has been turned ON.")
        else:
            print(f"{self.name} is already ON.")

    def turn_off(self):
       
        if self.is_on:
            self.is_on = False
            SmartDevice.active_devices -= 1
            print(f"{self.name} has been turned OFF.")
        else:
            print(f"{self.name} is already OFF.")

    def display_device_status(self):
        """Prints the name and current status (ON/OFF) of the device."""
        status = "ON" if self.is_on else "OFF"
        print(f"Device: {self.name}, Status: {status}")

 # Check initial counts
print(f"Total devices initially: {SmartDevice.total_devices}")
print(f"Active devices initially: {SmartDevice.active_devices}\n")

# Create new smart devices
tv = SmartDevice("Living Room TV")
lamp = SmartDevice("Bedroom Lamp")
speaker = SmartDevice("Kitchen Speaker")

# Check counts after creating devices
print(f"Total devices after setup: {SmartDevice.total_devices}")
print(f"Active devices after setup: {SmartDevice.active_devices}\n")

# Turn some devices on
tv.turn_on()
lamp.turn_on()

# Check active device count
print(f"\nActive devices now: {SmartDevice.active_devices}\n")

# Display status of all devices
tv.display_device_status()
lamp.display_device_status()
speaker.display_device_status()

# Turn a device off
print("\n--- Turning TV off ---")
tv.turn_off()
print(f"Active devices now: {SmartDevice.active_devices}")
tv.display_device_status()

#******************************************************************************

'''
Imagine you are a software developer for a
TV manufacturing company called "TechVision".
You need to create a DigitalTv class that will 
serve as a blueprint for all the smart TVs your company produces.

'''
'''
class DigitalTv:

    def __init__(self, brand, model, screen_size):
        self.brand = brand
        self.model = model
        self.screen_size = screen_size
        self.is_on = False
        self.channel = 1
        self.volume = 10

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"welcome!{self.brand} is turning on..")
        else:
            print(f"{self.brand} is already on..")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} TV is turning off.")
        else:
            print(f"{self.brand} is already off.")
    
    def display_info(self):
        print(f"info : \nBrand is {self.brand} \nModel: {self.model}\nScreen size is {self.screen_size}\n Tv status: {'on' if self.is_on else 'off'}")
        if self.is_on:
            print(f"The current channel no is {self.channel} and volume is {self.volume}")

    def change_channel(self, new_channel):
        if self.is_on:
            self.channel= new_channel
            print(f"The new channel is {new_channel}")
        else:
            print("cannot change channel,the TV is off")

    def adjust_volume(self, amount):
        
        if self.is_on:
            sum = self.volume + amount
            if sum>=0 and sum<=100:
                self.volume+=amount
            print(f"The current volume is {self.volume}")
        else:
            print("cannot adjust volume, the TV is off")
        

dgtv = DigitalTv("samsung", 2024, 45)
dgtv.turn_off()
dgtv.display_info()
dgtv.change_channel(55)
dgtv.adjust_volume(-90)

'''

