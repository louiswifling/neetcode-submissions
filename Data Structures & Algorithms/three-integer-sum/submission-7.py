class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)

        n = len(nums)


        triples = []
        last_num = 0


        print(nums)

        for i in range(n - 2): 

            if i > 0 and nums[i] == last_num: 
                continue

            last_num = nums[i]

            print(i)

            j = i + 1
            k = n - 1

            last_left = 0
            last_right = 0

            while j < k: 


                if nums[i] + nums[j] + nums[k] == 0: 
                    triples.append((nums[i], nums[j], nums[k]))
                    last_left = nums[j]
                    last_right = nums[k]
                    while j < n and nums[j] == last_left: 
                        j += 1
                    while k > i + 1 and nums[k] == last_right: 
                        k -= 1
                    
                    continue
                
                if nums[i] + nums[j] + nums[k] < 0: 
                    last_left = nums[j]
                    while j < n and nums[j] == last_left: 
                        j += 1
                    continue
                
                if nums[i] + nums[j] + nums[k] > 0: 
                    last_right = nums[k]
                    while k > i + 1 and nums[k] == last_right:  
                        k -= 1
                    continue

        return triples