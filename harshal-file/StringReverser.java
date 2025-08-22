
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
        String emptyArray = "";
     
        for (int i = 0; i < text.length(); i++) {
            char ch = text.charAt(i);//J a v a
            emptyArray = ch + emptyArray;
        }
        return emptyArray; // Placeholder
    }
}


