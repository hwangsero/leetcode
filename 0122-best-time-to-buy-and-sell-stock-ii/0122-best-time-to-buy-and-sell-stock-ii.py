class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, stock = 0, prices[0]

        for idx in range(1, len(prices)):
            if prices[idx] > stock:
                profit += (prices[idx] - stock)
            stock = prices[idx]
        return profit
        
