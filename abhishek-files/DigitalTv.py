class DigitalTv:
    def __init__(self, brand, model, screen_size):
        self.brand = brand
        self.model = model
        self.screen_size = screen_size
        self.is_on = False         # Default OFF
        self.channel = 1           # Default channel
        self.volume = 10           # Default volume
        self.is_muted = False      # Track mute state

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"Welcome! {self.brand} TV is turning on.")
        else:
            print(f"{self.brand} TV is already on.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} TV is turning off.")
        else:
            print(f"{self.brand} TV is already off.")

    def display_info(self):
        print(f"\n--- {self.brand} {self.model} ({self.screen_size}\") ---")
        if self.is_on:
            vol_status = "MUTED" if self.is_muted else self.volume
            print(f"Status: ON | Channel: {self.channel} | Volume: {vol_status}")
        else:
            print("Status: OFF")

    # --- Remote Features ---

    def change_channel(self, new_channel):
        if self.is_on:
            if new_channel > 0:
                self.channel = new_channel
                print(f"Channel changed to {self.channel}")
            else:
                print("Invalid channel number.")
        else:
            print("TV is OFF. Please turn it ON first.")

    def channel_up(self):
        if self.is_on:
            self.channel += 1
            print(f"Channel changed to {self.channel}")
        else:
            print("TV is OFF.")

    def channel_down(self):
        if self.is_on and self.channel > 1:
            self.channel -= 1
            print(f"Channel changed to {self.channel}")
        elif not self.is_on:
            print("TV is OFF.")
        else:
            print("Already at the lowest channel.")

    def volume_up(self):
        if self.is_on and self.volume < 100:
            self.is_muted = False
            self.volume += 1
            print(f"Volume increased to {self.volume}")
        elif not self.is_on:
            print("TV is OFF.")
        else:
            print("Volume is already at maximum.")

    def volume_down(self):
        if self.is_on and self.volume > 0:
            self.is_muted = False
            self.volume -= 1
            print(f"Volume decreased to {self.volume}")
        elif not self.is_on:
            print("TV is OFF.")
        else:
            print("Volume is already at minimum.")

    def mute(self):
        if self.is_on:
            self.is_muted = not self.is_muted
            state = "MUTED" if self.is_muted else f"{self.volume}"
            print(f"Volume is now {state}")
        else:
            print("TV is OFF.")
            
# Create a TV object
tv1 = DigitalTv("TechVision", "X200", 55)

# Display initial info
tv1.display_info()

# Turn on the TV
tv1.turn_on()
tv1.display_info()

# Turn on again (should show "already on")
tv1.turn_on()

# Turn off the TV
tv1.turn_off()
tv1.display_info()



tv = DigitalTv("TechVision", "X500", 65)

tv.display_info()

tv.turn_on()
tv.change_channel(5)
tv.channel_up()
tv.channel_down()

tv.volume_up()
tv.volume_down()
tv.mute()
tv.mute()

tv.turn_off()
tv.display_info()
