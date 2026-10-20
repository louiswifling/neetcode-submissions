class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n = len(s2)

        s1_map = {}
        for c in s1: 
            if c in s1_map: 
                s1_map[c] += 1
            else: 
                s1_map[c] = 1

        
        
        k = len(s1)

        if k > n: 
            return False
        


        problematic_letters = len(s1_map)

        for c in s2: 
            if c not in s1_map: 
                s1_map[c] = 0

        for c in s2[:k]: 
            if s1_map[c] == 0: 
                problematic_letters += 1
            s1_map[c] -= 1
            if s1_map[c] == 0: 
                problematic_letters -= 1
        
        if problematic_letters == 0: 
            return True

        for i in range(n - k): 
            
            c_remove = s2[i]
            c_add = s2[k + i]

            if s1_map[c_remove] == 0: 
                problematic_letters += 1
            s1_map[c_remove] += 1
            if s1_map[c_remove] == 0: 
                problematic_letters -= 1

            if s1_map[c_add] == 0: 
                problematic_letters += 1
            s1_map[c_add] -= 1
            if s1_map[c_add] == 0: 
                problematic_letters -= 1


            if problematic_letters == 0: 
                return True



        return False








        
        