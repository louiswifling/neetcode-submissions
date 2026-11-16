class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

        # DP[i][j] is the length of the longest common subsequence 
        # using the prefixes text1[:] and text2[:j]. 

        s1 = text1
        s2 = text2

        n = len(s1)
        m = len(s2)

        occurences = {}


        



        DP = [[0] * (m + 1) for _ in range(n + 1)] 




        for x in range(1, n + 1): 

            occurences[s1[x - 1]] = x - 1

            
            for y in range(1, m + 1): 

                c = s2[y - 1]


                
                DP[x][y] = DP[x][y - 1] 

                if c in occurences: 
                    DP[x][y] = max(
                        DP[x][y], 
                        1 + DP[occurences[c]][y - 1]
                    )

        
        print(DP)
        return DP[n][m]








        