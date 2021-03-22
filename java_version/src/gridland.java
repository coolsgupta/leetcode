import java.util.*;

public class gridland {
    public static List<String> getSafePaths(List<String> journeys){
        int[][] dp = new int[11][11];
        for (int i=0; i < 11; i++)
            for(int j=0; j<11; j++)
                dp[i][j] = 1;

        for (int i=1; i < 11; i++)
            for(int j=1; j<11; j++)
                dp[i][j] = dp[i-1][j] + dp[i][j-1];

        List<String> res = new ArrayList<String>();
        for (int i=1; i<journeys.size(); i++){
            char[] journey = journeys.get(i).toCharArray();
            int x = journey[0];
            int y = journey[1];
            int k = journey[2] + 1;
            StringBuilder result = new StringBuilder();

            while(x> 0 && y > 0){
                if (dp[x-1][y] >= k) {
                    result.append("H");
                    x -= 1;
                }
                else {
                    result.append("V");
                    k -= dp[x - 1][y];
                    y -= 1;
                }
            }
            while(y > 0){
                result.append("V");
                y-=1;
            }
            while(x>0){
                result.append("H");
                x-=1;
            }
            res.add(result.toString());
        }
        return res;

    }
}
