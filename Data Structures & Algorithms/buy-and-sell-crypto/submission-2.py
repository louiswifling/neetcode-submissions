class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        if n == 1: 
            return 0

        max_profit = 0

        cummax = prices[-1]

        for i in range(n - 2, -1, -1): 

            max_profit = max(max_profit, cummax - prices[i])
            cummax = max(prices[i], cummax)

        return max_profit

