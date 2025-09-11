package OOPS_CONCEPTS;

public class DigitalTv {
    
    private String brand;
    private String model;
    private int screenSize;
    private boolean isOn;
    private int channel;
    private int volume;

    //Constructor.....

    public DigitalTv(String brand, String model, int screenSize){
        this.brand = brand;
        this.model = model;
        this.screenSize = screenSize;

        this.isOn =false;
        this.channel = 1;
        this.volume = 10;
    }

    //Methods
 
    public void turnOn(){
        if(!isOn){
            isOn = true;
            System.out.println("welcome " + brand + "Tv is Turning On");
        }else{
            System.out.println(brand + "Tv is Already On");
        }
    }

    public  void turnOff(){
        if(isOn){
            isOn = false;  
            System.out.println(brand + "Tv is Turning Off...");

        }else{
            System.out.println(brand + "Tv is Already Off....");
        }
    }

    public void displayInfo(){
            System.out.println("brand : " + brand);
            System.out.println("Model : " + model);
            System.out.println("Screen Size : " + screenSize + "inch");

            if(isOn){
                System.out.println("Status : ON");
                System.out.println("Current Channel: " + channel);
                System.out.println("Current volume :" + volume);
            }else{
                System.out.println("Status : OFF");
            }
    }
// channel change
    public void changeChannel(int newchennal){
           if(isOn){
            channel = newchennal;
            System.out.println("The Chenl Changesd to " + channel);
           }else{
            System.out.println("Cannot change channel, the TV is off");
           }
    }
//Volume Adjustment
    public void adjustVolume(int amount){
        if(isOn){
            volume += amount;

             if (volume > 100) {
                volume = 100;
            } else if (volume < 0) {
                volume = 0;
            }

            System.out.println("Volume set to " + volume);
        } else {
            System.out.println("Cannot adjust volume, the TV is off.");
        }
    }

    
    
//Main Functions    
    public static void main(String[] args) {
        
        DigitalTv  tv = new DigitalTv("samsung", "SmartTv", 32);

        tv.displayInfo();
        // tv.turnOff();
        tv.turnOn();
        // tv.turnOff();
        tv.displayInfo();
        tv.changeChannel(54);
        tv.adjustVolume(0);
    }
}

