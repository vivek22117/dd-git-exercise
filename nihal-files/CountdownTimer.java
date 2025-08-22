public class CountdownTimer {

    public static void main(String[] args) {
        // --- Test Case ---
        System.out.println("Starting 5-second countdown:");
        countdown(5);        
        // Expected Output:
        // 5
        // 4
        // 3
        // 2
        // 1
        // Blast off!
    }

    // Your method here
    public static void countdown(int startNum) {
        while(startNum >=1){                              
           System.out.println(startNum);
           startNum--; // startnum =startnumber-1
        
        }
        System.out.println("Blast off!");
    }
}
