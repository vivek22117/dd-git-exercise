class DigitalTv:

  def __init__(self,brand,model,screen_size,):
    self.brand=brand
    self.model=model
    self.screen_size=screen_size
    self.is_on = False
    self.channel=1
    self.volume= 10

  def turn_on(self):
    if not self.is_on:
      self.is_on=True
      print(f"Welcome! {self.brand} tv is turnning on.")
    else:
      print(f"{self.brand} TV is already on")

  def turn_off(self):
    if self.is_on:
      self.is_on = False
      print(f"{self.brand} TV is turninng off")
    else:
      print(f"{self.brand} TV is already off")

  def display_info(self):
    print(f"TV Brand: {self.brand},Model: {self.model},Screen size: {self.screen_size}")
    current_status= "on TV " if  self.is_on else "off TV" 
    print(f"Device: {self.brand}, Status:{current_status}") 


  def change_channel(self,new_channel):
    if self.is_on == True:
      # self.channel += 1
      self.channel = new_channel
      print(f"{self.brand} TV channel is changed to new channel {self.channel}")
    else:
      print(f"{self.brand}TV is off. turn it on")
  
  def adjust_volume(self, amount):
    if self.is_on:
        self.volume += amount

        if self.volume < 0:
            self.volume = 0
        elif self.volume > 100:
            self.volume = 100

        print(f"{self.brand} is ON, volume is now {self.volume}")
    else:
        print(f"{self.brand} TV is OFF, cannot adjust volume")
  
#create an object of digitalTv
tv_1=DigitalTv("LG","OLED C1" ,"48 INCH") 
# tv_2=DigitalTv("SONY","Bravia X90j","68 INCH")
# tv_3=DigitalTv("TCL","Roku tv","55 INCH")


# change channel and see the status of tv
tv_1.turn_on()
tv_1.change_channel(10)
tv_1.turn_off()
tv_1.change_channel(5)
tv_1.display_info()


##Now change the volume of tv and check the status of tv
tv_1.turn_on()
tv_1.adjust_volume(10)
tv_1.adjust_volume(-5)
tv_1.adjust_volume(-50)
tv_1.adjust_volume(150)


 




