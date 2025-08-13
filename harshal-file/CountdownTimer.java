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
       for(int i=startNum;i>=0;i--)
       {
        System.out.println(i);
       }
    }
}
