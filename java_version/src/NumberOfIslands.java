public class NumberOfIslands {
    char[][] grid;
    int n;
    int m;

    public void dfs(int i, int j){
        if (0<=i && i<this.n && 0<=j && j<this.m && this.grid[i][j] == '1'){
            this.grid[i][j] = '0';
            this.dfs(i-1, j);
            this.dfs(i, j-1);
            this.dfs(i+1, j);
            this.dfs(i, j+1);
        }
    }

    public int numIslands(char[][] grid) {
        this.grid = grid;
        this.n = grid.length;
        this.m = grid[0].length;
        int islands = 0;

        for(int i=0; i<this.n; i++){
            for(int j=0; j<this.m; j++){
                if (this.grid[i][j] == '1'){
                    islands++;
                    this.dfs(i, j);
                }
            }
        }
        return islands;
    }
}
