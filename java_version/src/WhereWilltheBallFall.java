class Solution {
    public int[] findBall(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int[] pos = new int[m];
        for (int i = 0; i < m; i++){
            int x = 0;
            int y = i;
            while ( x < n){
                int newY = y + grid[x][y];
                if ( 0 <= newY && newY < m && grid[x][newY] == grid[x][y]){
                    y = newY;
                    x++;
                }
                else{
                    y = -1;
                    break;
                }
            }
            pos[i] = y;
        }
        return pos;
    }
}