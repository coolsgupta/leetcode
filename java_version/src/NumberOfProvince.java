public class NumberOfProvince {
    int[][] grid;
    int n;

    public void dfs(int i, int j){
        if (0<=i && i<this.n && 0<=j && j<this.n && this.grid[i][j] == 1){
            this.grid[i][j] = 0;
            this.grid[j][i] = 0;
            this.dfs(i-1, j);
            this.dfs(i, j-1);
            this.dfs(i+1, j);
            this.dfs(i, j+1);
        }
    }

    public int findCircleNum(int[][] isConnected) {
        this.grid = isConnected;
        this.n = isConnected.length;
        int provinces = 0;

        for(int i=0; i<this.n; i++){
            for(int j=0; j<this.n; j++){
                if (this.grid[i][j] == 1){
                    provinces++;
                    this.dfs(i, j);
                }
            }
        }
        return provinces;
    }
}
