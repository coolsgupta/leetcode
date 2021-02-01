public class NextPermutation {
    public void swap(int[] nums, int i, int j){
        int temp = nums[j];
        nums[j] = nums[i];
        nums[i] = temp;
    }

    public void nextPermutation(int[] nums) {
        int j = nums.length - 2;
        while(j>=0 && nums[j] >= nums[j+1])
            j--;

        if(j<0){
            Arrays.sort(nums);
        }
        else{
            int i = j;
            while(i<nums.length-1 && nums[i+1] > nums[j])
                i++;

            this.swap(nums, i, j);
            i = nums.length-1;
            j += 1;
            while(i>j){
                this.swap(nums, i, j);
                i--;
                j++;
            }
        }
    }
}
