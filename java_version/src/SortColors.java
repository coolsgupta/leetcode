public class SortColors {
    public void swap(int i, int j, int[] nums){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public void sortColors(int[] nums) {
        int x0 = 0;
        int x2 = nums.length - 1;
        int curr = 0;
        while(curr<=x2){
            if(nums[curr] == 0){
                swap(curr, x0, nums);
                x0++;
                curr++;
            }
            else if(nums[curr] == 2){
                swap(curr, x2, nums);
                x2--;
            }
            else{
                curr++;
            }
        }
    }
}
