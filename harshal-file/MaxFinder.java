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
        int max = 0;
        for (int i = 0; i < numbers.length-1; i++) {
            if (numbers[i + 1] > numbers[i]) {
                max = numbers[i + 1];
            }
        }
        return max; // Placeholder
    }
}