class Solution {    
    public int coinChange(int[] coins, int amount) {
        int[] reCoins = new int[amount + 1];
        Arrays.fill(reCoins, amount + 1);
        reCoins[0] = 0;
        
        for (int x: coins){
            for (int i = x; i <= amount; i++){
                reCoins[i] = Math.min(reCoins[i - x] + 1, reCoins[i]);
            }
        }
        return reCoins[amount] > amount? -1: reCoins[amount];
        
    }
}