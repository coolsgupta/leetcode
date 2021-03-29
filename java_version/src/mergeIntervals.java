class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0], b[0]));
        ArrayList<int[]> inter = new ArrayList<int[]>();
        inter.add(intervals[0]);
        int x = 0;
        for (int i = 1; i < intervals.length; i++){
            if (intervals[i][0] <= inter.get(x)[1]){
                if (intervals[i][1] > inter.get(x)[1])
                    inter.get(x)[1] = intervals[i][1];
            }
            else{
                inter.add(intervals[i]);
                x++;
            }
                
        }
        int[][] res = new int[inter.size()][2];
        for (int i=0; i< inter.size(); i++){
            res[i] = inter.get(i);
        }
        return res;
        
    }
}