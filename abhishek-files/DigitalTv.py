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

tv.turn_off()
tv.display_info()
