""" Task : Challenge: Create a SmartDevice class. Modify it to track the total and active devices in your house:

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
"""
class SmartDeivce:
    total_device =0
    active_device = 0
    def __init__(self,name):
        self.name = name
        self.is_on = True
        SmartDeivce.total_device += 1
    def turn_on(self,):
        if not self.is_on:
            self.is_on = True
            SmartDeivce.active_device+=1
            print(f"The {self.name} has been turend ON")
        else:
            print(f"{self.name} alredy Turn ON")
    def turn_off(self):
            if self.is_on:
                 self.is_on = False
                 SmartDeivce.active_device -= 1
                 print(f"{self.name} has been turn OFF")
            else:
                 print(f"{self.name} alredy turned OFF")
    def devices_status(self):
         if not self.is_on:
              status = "ON"
              print(f"Device: {self.name}, Status: {status}")
         else:
              status = "OFF" 
              print(f"Device: {self.name}, Status: {status}")     
         
         pass
print(f"Total devices after setup: {SmartDeivce.total_device}")
print(f"Total active device {SmartDeivce.active_device}")


tv = SmartDeivce("Living Room TV")
lamp = SmartDeivce("In Hall area")
ac = SmartDeivce("Second Room")

# Somedevice Turn on 
tv.turn_on()
tv.turn_off()
lamp.turn_on()
tv.devices_status()
lamp.devices_status()

# ac.turn_on()
# print(f"Total active device {SmartDeivce.active_device}")
# # Somedevice Turn OFF 
# lamp.turn_off()
# print(f"Total active device {SmartDeivce.active_device}")
# #Status for each devices 
# tv.devices_status()
# lamp.devices_status()
# ac.devices_status()

