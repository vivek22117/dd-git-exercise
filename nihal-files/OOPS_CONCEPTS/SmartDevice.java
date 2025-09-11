package OOPS_CONCEPTS;
public class SmartDevice {

    public static int totalDevices = 0;
    public static int activeDevices = 0;

    private String name;
    private boolean isOn;

    /**
     * Constructor for the SmartDevice class.
     */
    public SmartDevice(String name) {
        this.name = name;
        this.isOn = false; // Each device starts in the OFF state.

        SmartDevice.totalDevices++;
    }

    /**
     * Turns the device on and updates the active device count if it was off.
     */
    public void turnOn() {
        if (!this.isOn) {
            this.isOn = true;
            SmartDevice.activeDevices++;
            System.out.println(this.name + " has been turned ON.");
        } else {
            System.out.println(this.name + " is already ON.");
        }
    }

    /**
     * Turns the device off and updates the active device count if it was on.
     */
    public void turnOff() {
        if (this.isOn) {
            this.isOn = false;
            SmartDevice.activeDevices--;
            System.out.println(this.name + " has been turned OFF.");
        } else {
            System.out.println(this.name + " is already OFF.");
        }
    }

    /**
     * Prints the name and current status (ON/OFF) of the device.
     */
    public void displayDeviceStatus() {
        String status = this.isOn ? "ON" : "OFF";
        System.out.printf("Device: %s, Status: %s\n", this.name, status);
    }

    // --- Main method for Example Usage ---
    public static void main(String[] args) {
        // Check initial counts
        System.out.println("Total devices initially: " + SmartDevice.totalDevices);
        System.out.println("Active devices initially: " + SmartDevice.activeDevices + "\n");

        // Create new smart devices
        SmartDevice tv = new SmartDevice("Living Room TV");
        SmartDevice lamp = new SmartDevice("Bedroom Lamp");
        SmartDevice speaker = new SmartDevice("Kitchen Speaker");

        // Check counts after creating devices
        System.out.println("Total devices after setup: " + SmartDevice.totalDevices);
        System.out.println("Active devices after setup: " + SmartDevice.activeDevices + "\n");

        // Turn some devices on
        tv.turnOn();
        lamp.turnOn();

        // Check active device count
        System.out.println("\nActive devices now: " + SmartDevice.activeDevices + "\n");

        // Display status of all devices
        tv.displayDeviceStatus();
        lamp.displayDeviceStatus();
        speaker.displayDeviceStatus();

        // Turn a device off
        System.out.println("\n--- Turning TV off ---");
        tv.turnOff();
        System.out.println("Active devices now: " + SmartDevice.activeDevices);
        tv.displayDeviceStatus();
    }
}
