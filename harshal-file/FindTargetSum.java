/**
 * Given an array of integers nums and an integer target, return indices
 * of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution,
 * and you may not use the same element twice.
 *
 * Input: [4, 6, 1, 9, 3, 5, 0, 7, 2], Target Sum = 16
 * Output: [3, 7] # Index of “9” and “7” sums to 16
 */
public class FindTargetSum {

    public static int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] { i, j };
                }
            }
        }
        return new int[] {}; // No solution
    }

    public static void main(String[] args) {
        int nums[] = { 4, 6, 1, 9, 3, 5, 0, 7, 2 };
        int target = 16;
        int[] tar = twoSum(nums, target);
        System.out.println(tar[0] + ", " + tar[1]);

    }
}
