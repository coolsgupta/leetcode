public class Numberof1Bits {
    // using a bit mask
    public int hammingWeight(int n) {
        int ones = 0;
        int mask = 1;
        for(int i =0; i<32; i++){
            if((n&mask) != 0)
                ones++;
            mask <<= 1;
        }
        return ones;
    }
    // bit manipulation with n-1
    public int hammingWeight_2(int n) {
        int ones = 0;
        while(n!=0){
            ones += 1;
            n = n&(n-1);
        }
        return ones;
    }

}
