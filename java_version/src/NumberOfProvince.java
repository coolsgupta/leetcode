public class NumberOfProvince {
    int[][] grid;
    int n;

    public void dfs(int i, int j){
        for(int x=j; x<this.n; x++){
            if (this.grid[i][x] == 1){
                this.grid[i][x] = 0;
                this.grid[x][i] = 0;
                this.dfs(x, 0);
            }
        }
    }

    public int findCircleNum(int[][] isConnected) {
        this.grid = isConnected;
        this.n = isConnected.length;
        int provinces = 0;

        for(int i=0; i<this.n; i++){
            for(int j=0; j<this.n; j++){
                if (this.grid[i][j] == 1){
                    this.dfs(i, j);
                    provinces++;
                    break;
                }
            }
        }
        return provinces;
    }
}
