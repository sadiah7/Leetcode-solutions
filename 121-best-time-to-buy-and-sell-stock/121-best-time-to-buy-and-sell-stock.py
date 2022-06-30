class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) <= 1):
            return 0
        profit, cp = 0, prices[0]
        for price in prices:
            if(price < cp):
                cp = price
            else:
                profit = max(profit, price-cp)
        return profit