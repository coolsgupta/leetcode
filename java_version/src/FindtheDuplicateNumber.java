public class FindtheDuplicateNumber {
    public int findDuplicate(int[] nums) {
        Arrays.sort(nums);
        int i= 1;
        for(i=1; i<nums.length; i++)
            if(nums[i] == nums[i-1])
                break;

        return nums[i];
    }

    // using Floyd's Hare and Tortoise algorithms (for cycle detection in linked list)
    public int findDuplicateOptimized(int[] nums) {
        int hare = nums[0];
        int tortoise = nums[0];

        do{
            tortoise = nums[tortoise];
            hare = nums[nums[hare]];
        }while(hare != tortoise);
        tortoise = nums[0];
        while(hare != tortoise){
            hare = nums[hare];
            tortoise = nums[tortoise];
        }
        return hare;
    }
}
