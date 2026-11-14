class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        
        # for 0 <= i < n - 1, we have the following: 
        # profit_nocoin[i] = max(-prices[i] + profit_coin[i + 1], profit_nocoin[i + 1])

        # Also, profit_nocoin[n - 1] = 0

        # for 0 <= i < n - 2, we have the following: 
        # profit_coin[i] = max(profit_coin[i + 1], prices[i] + profit_nocoin[i + 2])

        # Also, profit_coin[n - 2] = max(profit_coin[i + 1], prices[i])
        # and profit_coin[n - 1] = prices[n - 1]
        
        profit_coin_tomorrow = prices[n - 1]
        profit_nocoin_tomorrow = 0
        profit_nocoin_overtomorrow = 0

        for i in range(n - 2, -1, -1): 
            profit_nocoin_today = max(-prices[i] + profit_coin_tomorrow, profit_nocoin_tomorrow)

            profit_coin_today = max(profit_coin_tomorrow, prices[i] + profit_nocoin_overtomorrow)

            profit_nocoin_overtomorrow = profit_nocoin_tomorrow
            profit_nocoin_tomorrow = profit_nocoin_today
            profit_coin_tomorrow = profit_coin_today

        
        return profit_nocoin_tomorrow