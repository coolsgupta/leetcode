class Solution {
    public int xorOperation(int n, int start) {
        int curr = start;
        int res = start;
        for(int i = 1; i< n; i++){
            curr += 2;
            res = res ^ curr;
        }
        return res;
    }
}