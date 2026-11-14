class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)

        current_reach = nums[0]

        if current_reach == 0: 
            return n == 1

        for i in range(1, n): 
            current_reach -= 1
            current_reach = max(current_reach, nums[i])

            if current_reach == 0: 
                return i == n - 1

        return True

