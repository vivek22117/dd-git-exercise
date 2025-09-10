'''
Challenge: Create a SmartDevice class. Modify it to track the total and active devices in your house:

Add two class attributes:
total_devices: Track total number of devices created, initialized to 0
active_devices: Track number of devices currently turned on, initialized to 0

Add one instance attribute:
name: To assign name to the new device

Implement these methods:
turn_on(): Increase active devices by 1
turn_off(): Decrease active devices by 1
display_device_status(): Prints the device name and its current status ON or OFF

Note:
total_devices increases in __init__
Methods should only update active_devices count

'''

class SmartDevice:
    #class attributes
    total_devices=0
    active_devices=0
    def __init__(self,name):
        self.name=name    # instance attribute
        self.is_on=False
        
        SmartDevice.total_devices += 1
        
    def turn_on(self):
        if not self.is_on:
            self.is_on=True
            SmartDevice.active_devices += 1
            print(f"{self.name} has been turn on...")
           
            
        else:
            print(f"{self.name} is already on ....")
            
    
    def turn_off(self):
        if self.is_on:
            self.is_on=False 
            SmartDevice.active_devices -= 1
            print(f"{self.name} has been turned off..")
        else:
            print(f"{self.name} is already off ....")
        
        
    def display_device_status(self):
        print(f"Device name : {self.name} and status : {'ON' if self.is_on else 'OFF' } ")
        



# --- Example Usage ---

# Check initial counts
print(f"Total devices initially: {SmartDevice.total_devices}")
print(f"Active devices initially: {SmartDevice.active_devices}\n")

# # Create new smart devices
tv = SmartDevice("Living Room TV")
lamp = SmartDevice("Bedroom Lamp")
speaker = SmartDevice("Kitchen Speaker")

# # Check counts after creating devices
print(f"Total devices after setup: {SmartDevice.total_devices}")
print(f"Active devices after setup: {SmartDevice.active_devices}\n")

# # Turn some devices on
tv.turn_on()
lamp.turn_on()

# # Check active device count
print(f"\nActive devices now: {SmartDevice.active_devices}\n")

# # Display status of all devices
tv.display_device_status()
lamp.display_device_status()
speaker.display_device_status()

# # Turn a device off
print("\n--- Turning TV off ---")
tv.turn_off()
print(f"Active devices now: {SmartDevice.active_devices}")
tv.display_device_status()


