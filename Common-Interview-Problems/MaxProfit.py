"""
Determine the best time to buy and sell a stock
"""

def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        minBuy = prices[0]
        maxProf = 0
        for price in prices:
            if price < minBuy:
                minBuy = price
            elif price - minBuy > maxProf:
                maxProf = price - minBuy
        return maxProf