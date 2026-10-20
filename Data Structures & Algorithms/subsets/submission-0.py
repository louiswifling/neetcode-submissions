
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        


        n = len(nums)

        result = []




        current = set()

        
        while True: 


            result.append(list(current))

            change_index = n - 1
            while change_index >= 0: 
                if nums[change_index] not in current: 
                    break
                else: 
                    change_index -= 1
            if change_index == -1: 
                return result
            
            current.add(nums[change_index])
            for i in range(change_index + 1, n): 
                current.remove(nums[i])
            



            
            








