public class MaximunSubarray {
    public int maxSubArray(int[] nums) {
        int curr_sum = nums[0];
        int max_sum = curr_sum;
        for (int i = 1; i < nums.length; i++) {
//            curr_sum += nums[i];
//            if (nums[i] > curr_sum) {
//                curr_sum = nums[i];
//            }
//            if (max_sum < curr_sum)
//                max_sum = curr_sum;
            curr_sum = Math.max(curr_sum, curr_sum + nums[i]);
            max_sum = Math.max(curr_sum, max_sum);
        }

        return max_sum;
    }
}
