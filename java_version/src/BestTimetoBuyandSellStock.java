public class BestTimetoBuyandSellStock {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int minPrice = Integer.MAX_VALUE;
        for (int x: prices){
            if (x < minPrice)
                minPrice = x;

            else if (x - minPrice > maxProfit)
                maxProfit = x - minPrice;
        }
        return maxProfit;
    }
}
