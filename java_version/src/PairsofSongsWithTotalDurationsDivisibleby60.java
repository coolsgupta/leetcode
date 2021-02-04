public class PairsofSongsWithTotalDurationsDivisibleby60 {
    public int numPairsDivisibleBy60(int[] time) {
        int[] rem = new int[60];
        int count = 0;
        for(int x: time){
            int c_rem = x%60;
            if(c_rem == 0)
                count += rem[0];
            else
                count += rem[60 - c_rem];
            rem[c_rem] += 1;
        }
        return count;
    }
}
