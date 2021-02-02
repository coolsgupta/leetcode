public class SortColors {
    public void swap(int i, int j, int[] nums){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public void sortColors(int[] nums) {
        int x = 0;
        for(int i=0; i<3; i++){
            for(int j=x; j<nums.length; j++){
                if(nums[j] == i){
                    this.swap(x, j, nums);
                    x++;
                }
            }
        }
    }
}
