class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        











        n = len(numbers)


        left = 0
        right = n - 1

        while left < right: 
            s = numbers[left] + numbers[right]
            if s < target: 
                left += 1
                continue
            if s > target: 
                right -= 1
                continue
            return [left + 1, right + 1]









            