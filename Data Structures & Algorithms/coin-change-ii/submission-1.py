class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        



        # DP[l][a] is number of combinations to build a using only coins 
        # 0, ..., l - 1

        DP = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        DP[0][0] = 1


        for l in range(1, len(coins) + 1): 
            for a in range(0, amount + 1): 
                
                if a - coins[l - 1] >= 0: 
                    DP[l][a] = DP[l - 1][a] + DP[l][a - coins[l - 1]]

                else: 
                    DP[l][a] = DP[l - 1][a]



        return DP[len(coins)][amount]