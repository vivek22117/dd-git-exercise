public class ContainDuplicate {

    public static boolean containerduplicate(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int[] number01 = { 1, 2, 3, 1 };
        int[] number02 = { 1, 2, 3, 4 };

        System.out.println(containerduplicate(number01));
        System.out.println(containerduplicate(number02));

    }
}
