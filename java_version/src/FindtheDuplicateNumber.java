public class FindtheDuplicateNumber {
    public int findDuplicate(int[] nums) {
        Arrays.sort(nums);
        int i= 1;
        for(i=1; i<nums.length; i++)
            if(nums[i] == nums[i-1])
                break;

        return nums[i];
    }
}
