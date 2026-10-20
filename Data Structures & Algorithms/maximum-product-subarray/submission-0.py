class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n = len(nums)


        DPMax = [0] * n
        DPMin = [0] * n

        for i in range(n): 
            if i == 0: 
                DPMin[0] = nums[0]
                DPMax[0] = nums[0]
                continue
            
            if nums[i] >= 0: 
                DPMax[i] = nums[i] * max(1, DPMax[i - 1])
                DPMin[i] = nums[i] * min(1, DPMin[i - 1])
            if nums[i] < 0: 
                DPMin[i] = nums[i] * max(1, DPMax[i - 1])
                DPMax[i] = nums[i] * min(1, DPMin[i - 1])
        

        return max(DPMax)
            