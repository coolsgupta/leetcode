class Solution {
    public int firstMissingPositive(int[] nums) {
        boolean flag = false;
        for (int x: nums){
            if (x == 1){
                flag = true;
                break;
            }
        }
        
        if (!flag)
            return 1;
        
        if (nums.length == 1)
            return 2;
        
        for(int i = 0; i < nums.length; i++)
            if (nums[i] < 1 || nums[i] > nums.length)
                nums[i] = 1;
        
        for(int i = 0; i < nums.length; i++){
            int x = Math.abs(nums[i]);
            if (x == nums.length)
                nums[0] = - Math.abs(nums[0]);
            
            else
                nums[x] = - Math.abs(nums[x]);
        }
        
        for(int i = 1; i < nums.length; i++){
            if (nums[i] > 0)
                return i;
        }
        
        if(nums[0] > 0)
            return nums.length;
        
        return nums.length + 1;
        
    }
}