public class MissingNumber {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int req_sum = n*(n+1)/2;
        for (int x:nums)
            req_sum -= x;
        return req_sum;
    }

}
