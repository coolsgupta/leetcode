class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            if price - min_price > profit:
                profit = price - min_price
        return profit
