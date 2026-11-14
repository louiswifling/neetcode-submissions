class Solution:
    def rob(self, nums: List[int]) -> int:
        

        n = len(nums)

        # profit_rob[i] = nums[i] + profit_norob[i + 1]
        # profit_norob[i] = max(profit_rob[i + 1], profit_norob[i + 1])


        profit_rob = nums[n - 1]
        profit_norob = 0

        for i in range(n - 2, -1, -1): 
            profit_rob_new = nums[i] + profit_norob
            profit_norob_new = max(profit_rob, profit_norob)

            profit_rob = profit_rob_new
            profit_norob = profit_norob_new

        
        return max(profit_rob, profit_norob)