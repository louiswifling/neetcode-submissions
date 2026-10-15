class Solution:
    def climbStairs(self, n: int) -> int:
        

        if n == 1: 
            return 1
        if n == 2: 
            return 2


        prev = 1
        current = 2

        for i in range(n - 2): 
            tmp = prev + current

            prev = current
            current = tmp
        
        return current
        
