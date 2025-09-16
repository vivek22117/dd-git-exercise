class DigitalTv :
    total_devices = 0
    active_devices = 0

    def __init__(self,brand,model,screen_size):
        self.brand = brand
        self.model = model
        self.screen_size = screen_size
        self.is_on = False
        self.channel = 1
        self.volume = 10
        DigitalTv.total_devices += 1
    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            DigitalTv.active_devices +=1
            print(f"Welcome! {self.brand} TV is turning on.")
        else:
            print(f"{self.brand} is alredy on")
    def turn_off(self):
        if self.is_on:
            self.is_on = False
            DigitalTv.active_devices -= 1
            print(f"Wlecome {self.brand} Tv is turnning OFF")
        else:
            print(f"{self.brand} is alredy turn OFF")
    def display_info(self):
        if self.is_on:
            status = "ON"
            print(f"info \nBrand is {self.brand} \nModel: {self.model}\nScreen size is {self.screen_size}\nTv status: {status}")
        else:
            status = "OFF"
            print(f"INFO \nBrand is {self.brand} \nModel: {self.model}\nScreen size is {self.screen_size}\nTv status: {status}")
    def change_channel(self,new_channel):
        if self.is_on:
            self.channel = new_channel
            print(f"The new channel is {new_channel}")
        else:
            print(f"Cannot chnage the channel Tv is OFF")
    def adjust_volume(self,amount):
        if self.is_on:
            sum = self.volume+amount
            if sum>=0 and sum<=100:
                self.volume+=amount
            print(f"The current volume is {self.volume}")
        else:
            print("cannot adjust volume, the TV is off")




print(f"Total number of devices {DigitalTv.total_devices}")
dgtv = DigitalTv("samsung", 2024, 45)

dgtv.turn_on()
dgtv.turn_off()
dgtv.display_info()
dgtv.change_channel(12)
dgtv.adjust_volume(101)

print(f"Total number of devices {DigitalTv.total_devices}")
print(f"Total number of active devices {DigitalTv.active_devices}")