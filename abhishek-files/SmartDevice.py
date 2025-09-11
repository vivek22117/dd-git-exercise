class SmartDevice:
    # Class attributes
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
        status = "ON" if self.is_on else "OFF"
        print(f"Device: {self.name}, Status: {status}")


# Example usage
fan = SmartDevice("Fan")
tv = SmartDevice("Television")

fan.turn_on()
tv.turn_on()
fan.display_device_status()
tv.display_device_status()

print(f"Total Devices: {SmartDevice.total_devices}")
print(f"Active Devices: {SmartDevice.active_devices}")

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

print("hellow")