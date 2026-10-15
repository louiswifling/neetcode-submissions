class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        if amount == 0: 
            return 0
        
        DP = [-1] * (amount + 1)

        DP[0] = 0

        for i in range(1, amount + 1): 
            min_coins = -1
            for coin in coins: 
                if coin > i: 
                    continue
                
                if DP[i - coin] != -1: 
                    if min_coins == -1: 
                        min_coins = DP[i - coin] + 1
                    else: 
                        min_coins = min(min_coins, DP[i - coin] + 1)
            DP[i] = min_coins
        
        return DP[-1]



        