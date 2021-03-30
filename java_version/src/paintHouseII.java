class Solution {
    public int minCostII(int[][] costs) {
        int n = costs.length;
        int k = costs[0].length;
        for (int i = 1; i < n; i++){
            int[] prevMin = {-1, -1};
            for (int c = 0; c < k; c++){
                if (prevMin[0] == -1 || costs[i - 1][c] < costs[i - 1][prevMin[0]]){
                    prevMin[1] = prevMin[0];
                    prevMin[0] = c;
                }
                else if (prevMin[1] == -1 || costs[i - 1][c] < costs[i - 1][prevMin[1]]){
                    prevMin[1] = c;
                }
            }

            for (int j = 0; j < k; j++){
                costs[i][j] += costs[i-1][(j == prevMin[0])? prevMin[1]: prevMin[0]];
            }
        }
        
        int res = costs[n-1][0];
        for (int x: costs[n-1])
            res = Math.min(res, x);
        
        return res;

    }
}