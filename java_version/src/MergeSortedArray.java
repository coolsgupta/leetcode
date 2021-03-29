class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m + n - 1;
        int x = m - 1;
        int y = n - 1;
        
        while(i >= 0){
            if ( x == -1 || (y != -1 && nums1[x] <= nums2[y])){
                nums1[i] = nums2[y];
                y--;
            }
            else{
                nums1[i] = nums1[x];
                x--;
            }
            i--;
        }
    }
}