import java.util.*;

public class MaximumOrderVolume {
    public static int phoneCalls(List<Integer> start, List<Integer> duration, List<Integer> volume){
        List <Integer> endtime = new ArrayList<Integer>();

        for (int i=0; i<duration.size(); i++){
            endtime.add(start.get(i) + duration.get(i));
        }

        int max_endTime = Collections.max(endtime);
        int[][] dp = new int[duration.size() + 1][max_endTime + 1];
        for (int i=0; i <= duration.size(); i++)
            for(int j=0; j<=max_endTime; j++)
                dp[i][j] = 0;

        for (int i=1; i <= duration.size(); i++)
            for(int j=1; j<=max_endTime; j++)
                dp[i][j] = Math.max(Math.max(dp[i-1][j], dp[i][j-1]), volume.get(i) + dp[i][start.get(i)-1]);

        return dp[duration.size()][max_endTime];
    }
}


[[]]