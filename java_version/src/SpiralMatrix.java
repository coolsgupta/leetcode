public class SpiralMatrix {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<Integer>();
        if (matrix.length == 0)
            return res;

        int rows = matrix.length;
        int cols = matrix[0].length;
        int r1 = 0, r2 = rows-1;
        int c1 = 0, c2 = cols-1;

        while(r1<=r2 && c1<=c2){
            for(int i = c1; i<=c2; i++) res.add(matrix[r1][i]);
            for(int i = r1 + 1; i<=r2; i++) res.add(matrix[i][c2]);

            if (r1 < r2 && c1 < c2){
                for(int i = c2 - 1; i>=c1; i--) res.add(matrix[r2][i]);
                for(int i = r2 - 1; i>r1; i--) res.add(matrix[i][c1]);
            }
            r1++;
            c1++;
            r2--;
            c2--;
        }
        return res;
    }
}
