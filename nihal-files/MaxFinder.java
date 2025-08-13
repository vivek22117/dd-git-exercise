public class MaxFinder {

    public static void main(String[] args) {
        // --- Test Cases ---
        int[] numbers1 = { 3, 41, 12, 9, 74, 15 };
        System.out.println("The max number is: " + findMax(numbers1)); // Expected: 74

        int[] numbers2 = { -10, -5, -2, -1 };
        System.out.println("The max number is: " + findMax(numbers2)); // Expected: -1
    }

    // Your method here
    public static int findMax(int[] numbers) {
        int max = numbers[0]; // start with first element
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[i] > max) {
                max = numbers[i]; // update max if current is bigger
            }
        }
        return max;// placeholder
    }

    
}
