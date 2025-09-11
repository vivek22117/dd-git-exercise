##Create a SmartDevice class. Modify it to track the total and active devices in your house

class SmartDevice:
  total_devices=0
  active_devices=0

  def __init__(self,name):
    self.name=name
    self.is_on=False

    SmartDevice.total_devices += 1


  def turn_on(self):
    #if device is off then turn it on
    if not self.is_on:
       self.is_on= True
       SmartDevice.active_devices +=1
       print(f"the {self.name} has been turn on")
    else:
        print(f"the {self.name} is already on.")

  def turn_off(self):
    if self.is_on:
        self.is_on = False
        SmartDevice.active_devices -=1
        print(f"the {self.name} has been turn off")
    else:
        print(f"the {self.name} is already off")

  def displaydevice_status(self):
     status= "on device " if  self.is_on else "off device"  
     print(f"Device: {self.name}, Status:{status}")   



#initial devices activity
print(f"Total devices initially: {SmartDevice.total_devices}")
print(f"Active device initially: {SmartDevice.active_devices} \n")

#Add new devices 
POP_light = SmartDevice("POP_light")
tv = SmartDevice("Hall TV")
speaker = SmartDevice("TV speakers")
vaccum_cleaner = SmartDevice("cleaning vaccum_cleaner") 
table_lamp = SmartDevice("studyroom table_lamp")   

#check counts after  creating devices
print(f"total devices after setup: {SmartDevice.total_devices}")
print(f"Active devices after setup : {SmartDevice.active_devices} \n")

#turn some devices on
tv.turn_on()
table_lamp.turn_on()
POP_light.turn_on()


#check active device count
print(f"Active devices now: {SmartDevice.active_devices} \n")

# vaccum_cleaner.turn_off()
# table_lamp.turn_off()

tv.displaydevice_status()
table_lamp.displaydevice_status()
speaker.displaydevice_status()

#turn a devices off
print(f"\n  ----Turning tv off")
tv.turn_off()
print(f"active devices now: {SmartDevice.active_devices}")
tv.displaydevice_status()


