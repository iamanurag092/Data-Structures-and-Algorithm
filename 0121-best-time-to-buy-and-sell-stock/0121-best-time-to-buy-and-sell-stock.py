class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP=prices[0]
        profit = 0
        for price in prices:
            minP=min(minP,price)
            profit=max(profit,price-minP)
        

        return profit
