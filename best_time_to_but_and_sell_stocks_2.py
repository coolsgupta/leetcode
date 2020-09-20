class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        c_profit = 0
        profit = 0
        last_min = prices[0]
        for price in prices[1:]:
            new_prof = price - last_min
            if new_prof >= c_profit:
                c_profit = new_prof

            else:
                profit += c_profit
                last_min = price
                c_profit = 0

        if c_profit:
            profit += c_profit

        return profit
