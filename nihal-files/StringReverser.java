public class StringReverser {

    public static void main(String[] args) {
        // --- Test Cases ---
        String original1 = "engineer";
        String result1 = bruteForceReverse(original1);
        System.out.println("Reversed: " + result1); // Expected: reenigne

        String original2 = "Java";
        String result2 = bruteForceReverse(original2);
        System.out.println("Reversed: " + result2); // Expected: avaJ
    }

    // Your method here
    public static String bruteForceReverse(String text) {
        StringBuilder reversed = new StringBuilder();
        for (int i = text.length() - 1; i >= 0; i--) {
            char ch = text.charAt(i);
            reversed.append(ch); // add it to the reversed string
        }
        return reversed.toString();// // Placeholder
    }

}
