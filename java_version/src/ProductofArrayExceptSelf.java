public class ProductofArrayExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] left = new int[n];
        int[] right = new int[n];
        left[0] = 1;
        right[n-1] = 1;
        for (int i=1; i<n; i++){
            left[i] = left[i-1]*nums[i-1];
            right[n-i-1] = right[n-i]*nums[n-i];
        }
        for(int i=0; i< n; i++)
            nums[i] = left[i]*right[i];
        return nums;
    }
}
