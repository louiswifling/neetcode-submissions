class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        

        # DP[i][j] is number of subsequences of s[:i] that are equal to 
        # t[:j]

        # Then DP[i][j] = DP[i - 1][j] (+ DP[i - 1][j - 1])


        # In fact we only need to maintain the row DP[i][.]


        n = len(s)
        m = len(t)

        ROW = [0] * (m + 1)

        ROW[0] = 1


        for i in range(1, n + 1): 






            for j in range(m, 0, -1): 

                if s[i - 1] == t[j - 1]: 
                    ROW[j] += ROW[j - 1]
            


        return ROW[m]




